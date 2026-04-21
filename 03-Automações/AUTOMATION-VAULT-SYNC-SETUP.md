# Vault Sync Automation Setup Synchronization system: MAC (Obsidian) ↔ VPS (Server) ↔ GitHub (Source of Truth) --- ## Architecture ```
MAC (Local)
├── Obsidian Vault
│ └── Auto-commit on save (git hooks)
└── Git push to GitHub ↓
GitHub Repository
├── rankpanda-growth-system-vault
└── Webhook triggers VPS sync ↓
VPS (Server)
├── Clone/pull latest from GitHub
├── Update cached version
├── Accessible to Claude agents
└── Notifications to Discord
``` --- ## Setup Steps ### 1. MAC — Local Git Configuration **Prerequisites:**
- Git installed
- Obsidian vault at: `/Users/rankpanda/Shopify RankPanda APP - Oficial 2026/vault/`
- GitHub token with repo access **Steps:** ```bash
cd /Users/rankpanda/Shopify\ RankPanda\ APP\ -\ Oficial\ 2026/vault/ # Initialize git (if not already done)
git init
git remote add origin https://github.com/rankpandaseo/rankpanda-growth-system-vault.git
git branch -M main # Configure git user
git config user.email "geral@rankpanda.pt"
git config user.name "RankPanda AI System" # Create git hooks for auto-commit on file change
mkdir -p .git/hooks
``` **Create `.git/hooks/post-merge` (auto-commit after manual edits):** ```bash
#!/bin/bash
# Auto-commit changes after merge/pull 
VAULT_DIR="/Users/rankpanda/Shopify RankPanda APP - Oficial 2026/vault"
cd "$VAULT_DIR"

if [ -n "$(git status -s)" ]; then
  git add -A
  git commit -m "Auto-sync: Vault update from Obsidian [$(date -u +%Y-%m-%dT%H:%M:%SZ)]"
  git push origin main
fi
``` Make executable:
```bash
chmod +x .git/hooks/post-merge
``` **Create `.git/hooks/pre-push` (validate before push):** ```bash
#!/bin/bash
# Quick validation before push VAULT_DIR="/Users/rankpanda/Shopify RankPanda APP - Oficial 2026/vault"
cd "$VAULT_DIR" # Check that MEMORY.md is not corrupted
if ! grep -q "Memory Index" MEMORY.md 2>/dev/null; then echo "❌ MEMORY.md is corrupted! Aborting push." exit 1
fi echo "✅ Pre-push validation passed"
exit 0
``` Make executable:
```bash
chmod +x .git/hooks/pre-push
``` **Obsidian Settings** (if using Git plugin):
- Install "Obsidian Git" plugin
- Configure auto-commit: every 1 minute (or on save)
- Configure auto-pull: every 2 minutes
- Set commit message: "Obsidian auto-sync: {date} {time}" --- ### 2. GitHub — Webhook Configuration **Create webhook to notify VPS on push:** 1. Go to: https://github.com/rankpandaseo/rankpanda-growth-system-vault/settings/hooks
2. Click "Add webhook"
3. Configure: - **Payload URL:** `https://[VPS-IP]:9000/webhooks/vault-sync` - **Content type:** `application/json` - **Events:** "Just the push event" - **Secret:** [generate random string, store in VPS env] --- ### 3. VPS — Sync & Deployment **Prerequisites:**
- VPS with Node.js, git, ssh access
- Webhook receiver service running **Webhook Handler** (`/server/webhooks/vault-sync.js`): ```javascript
import express from 'express';
import crypto from 'crypto';
import { execSync } from 'child_process'; const router = express.Router();
const VAULT_WEBHOOK_SECRET = process.env.VAULT_WEBHOOK_SECRET;
const VAULT_REPO_PATH = process.env.VAULT_REPO_PATH || '/var/rankpanda/vault'; router.post('/vault-sync', (req, res) => { // Verify webhook signature const signature = req.headers['x-hub-signature-256']; const payload = JSON.stringify(req.body); const hash = 'sha256=' + crypto .createHmac('sha256', VAULT_WEBHOOK_SECRET) .update(payload) .digest('hex'); if (signature !== hash) { return res.status(401).json({ error: 'Unauthorized' }); } try { // Pull latest from GitHub execSync(`cd ${VAULT_REPO_PATH} && git pull origin main`, { stdio: 'inherit' }); // Notify Discord const discordNotify = async () => { await fetch(process.env.DISCORD_WEBHOOK_URL, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ content: '✅ Vault synced from GitHub (VPS updated)' }) }); }; discordNotify(); res.json({ status: 'ok', message: 'Vault synced' }); } catch (error) { console.error('Vault sync error:', error); res.status(500).json({ error: error.message }); }
}); export default router;
``` **Cron Job** (for periodic pulls, failsafe): ```bash
# Add to crontab (every 5 minutes)
*/5 * * * * cd /var/rankpanda/vault && git pull origin main >> /var/log/vault-sync.log 2>&1
``` --- ### 4. Discord Notifications **Notify on sync events:** ```javascript
// In vault-sync.js after successful pull
const notifyDiscord = async (message) => { const webhook = process.env.DISCORD_VAULT_WEBHOOK; await fetch(webhook, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ content: message }) });
}; // Examples:
// notifyDiscord('✅ Vault synced: 5 files updated');
// notifyDiscord('⚠️ Vault sync conflict detected, manual review needed');
``` --- ## Environment Variables (VPS) Add to `.env` on VPS: ```
VAULT_REPO_PATH=/var/rankpanda/vault
VAULT_WEBHOOK_SECRET=super-secret-string
DISCORD_VAULT_WEBHOOK=https://discord.com/api/webhooks/...
``` --- ## Monitoring ### Health Check **Endpoint:** `GET /api/vault/sync-status` ```javascript
router.get('/sync-status', async (req, res) => { try { const lastCommit = execSync( `cd ${VAULT_REPO_PATH} && git log -1 --format=%ai`, { encoding: 'utf-8' } ); const status = execSync( `cd ${VAULT_REPO_PATH} && git status --porcelain`, { encoding: 'utf-8' } ); res.json({ status: status ? 'dirty' : 'clean', lastSync: lastCommit.trim(), changes: status ? status.split('\n').length : 0 }); } catch (error) { res.status(500).json({ error: error.message }); }
});
``` ### Logs Monitor sync status:
```bash
tail -f /var/log/vault-sync.log
``` --- ## Conflict Resolution **If merge conflicts occur:** 1. **VPS detects conflict:** ```bash cd /var/rankpanda/vault git status # Shows conflicts ``` 2. **Discord notification:** ``` ⚠️ Vault sync CONFLICT Branch: main Files: memory/xxx.md, vault/yyy.md Action: Manual merge required ``` 3. **Human resolves:** ```bash cd /var/rankpanda/vault # Manually fix conflicts git add . git commit -m "Resolve vault sync conflict" git push origin main ``` 4. **Resume automation** --- ## Disaster Recovery **Backup strategy:** ```bash
# Daily backup (add to crontab)
0 2 * * * tar -czf /backups/vault-$(date +%Y%m%d).tar.gz /var/rankpanda/vault/
``` **Restore from backup:** ```bash
cd /var/rankpanda/vault
tar -xzf /backups/vault-20260418.tar.gz
``` --- ## Testing **Manual test:** ```bash
# On MAC:
cd /Users/rankpanda/Shopify\ RankPanda\ APP\ -\ Oficial\ 2026/vault/
echo "Test commit $(date)" >> test.md
git add .
git commit -m "Test sync"
git push origin main # On VPS:
curl http://localhost/api/vault/sync-status
# Should show recent last sync # In Discord:
# Should see "✅ Vault synced" message
``` --- **Version:** 1.0 **Status:** Implementation Ready **Owner:** RankPanda DevOps
