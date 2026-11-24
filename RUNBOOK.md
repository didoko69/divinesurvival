# Automated episode run (scheduled task reads this)

Owner: Daniel. He does NOT review before posting — quality gate is you. If anything fails, do not upload; email him what failed.

1. Setup: repo cloned at /home/claude/divinesurvival. `cd` there, run `bash tools/setup.sh`.
2. Decide the episode: read SERIES.md (plan + status table), EPISODES.md (posted log), PERFORMANCE.md (latest learnings — apply them).
   Next episode = first "planned" row. Episode id like s1e2.
3. Write `episodes/<ep>/shots.py` following SERIES.md format rules and ENGINE.md. Also `thumb.json` ({"line1","line2","glow"}) and
   `thumb_shots.json` (shot 0 = inset scene, shot 1 = main scene with the characters big; see episodes/s1e1). New locations → `ep.js`.
4. Copy engine into work dir and run the mandatory frame check (ENGINE.md). Fix problems.
5. `bash tools/make.sh <ep>` (~30–40 min). Then extract 6 frames from out/<ep>/video.mp4 with ffmpeg and look at them, and check duration 6.5–11 min.
6. Write `episodes/<ep>/package.json`: {"title","description","tags":[...],"pinned_comment"}. Title pattern "Zombie Outbreak: <hook> | S1E2". Description: 2-line hook, chapters, "New episodes Mon/Wed/Fri", 3 hashtags. Tags 12–18 (zombie outbreak survival, zombie apocalypse survival, zombie survival story, zombie outbreak 30 days, 30 days trapped, animated survival story, stick figure animation, divine survival …).
7. Commit episodes/<ep>/ and push to main.
8. Host files (GitHub releases are blocked for these sessions — use the orphan `media` branch, replaced every run so the repo stays small):
   ```
   rm -rf /home/claude/media && mkdir /home/claude/media && cd /home/claude/media && git init -q -b media
   cp /home/claude/divinesurvival/out/<ep>/video.mp4 /home/claude/divinesurvival/out/<ep>/thumbnail.jpg .
   git add -A && git -c user.name=Claude -c user.email=noreply@anthropic.com commit -qm "media <ep>"
   git remote add origin https://github.com/didoko69/divinesurvival && git push -q -f origin media
   curl -sI https://raw.githubusercontent.com/didoko69/divinesurvival/media/video.mp4 | head -1   # must be 200 (wait ~10 s if 404)
   ```
   URLs: https://raw.githubusercontent.com/didoko69/divinesurvival/media/video.mp4 and …/media/thumbnail.jpg  (video must stay < 95 MB)
9. Upload with Zapier (YouTube app, action upload_video, tool_name youtube_upload_video): title, description, video=<video URL>, thumbnail=<thumb URL>,
   tags, privacy_status "public", category_id "1" (Film & Animation), made_for_kids "false", default_language "en", notify_subscribers "true".
   If the thumbnail did not apply, use action upload_video_thumbnail with the returned video id.
10. Update SERIES.md status (POSTED date) and EPISODES.md (ep, date, title, video id/URL). Commit + push.
11. Email Daniel via Zapier Gmail (send email) to didoko289@gmail.com: subject "✅ New episode live: <title>", body = link + pinned comment text to paste.
    Also send a push notification if available.
On failure at any step: no upload; email subject "⚠️ Episode <ep> failed" with the reason; leave work committed on a branch if useful.
