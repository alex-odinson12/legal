# Privacy Policy for Restore Old Photos: Colorize (Restina)

Effective date: {{EFFECTIVE_DATE}}. Android app, package com.restina.app.

## Who we are

Fablewood Studio publishes Restore Old Photos: Colorize (also shown as Restina) on Google Play (the App). For privacy questions or a data request, write to [quicklysearch.bot@gmail.com](mailto:quicklysearch.bot@gmail.com).

The App restores old photographs: it repairs damage, colourises black-and-white pictures, removes scratches, lightens dark photos and can turn a photo into a short video. This page explains what the App collects, who receives it and how long it is kept. There is no account and no registration.

## Photos you send

Before the first photo leaves your phone, the App asks your permission and names the companies that will receive it. You can withdraw that permission at any time in Menu → Sending photos → Withdraw permission. Nothing new is sent after that until you allow it again. Photos already sent cannot be recalled.

You choose each photo through Android's photo picker or take it with the App's camera screen. The App does not read your photo library. Before sending, the App prepares a smaller JPEG copy and removes its metadata, including EXIF and GPS location.

The photo travels over HTTPS to our server (api.restina.org, hosted on Cloudflare). Our server passes it to fal.ai, our processing partner, which sends it to the company running the model:

- Restore, Colourise, Scratches and Lighten send the photo to **OpenAI**, which returns an edited photo.
- Animate sends the photo to **PixVerse**, which returns a short video made from it.

The finished photo or video is delivered to the App through our own server, after we check that the request belongs to the device that created it. We never give out the provider's own link to your result.

Colourising means the model chooses colours, including skin, hair and clothing tones, that are plausible for the picture. They are an estimate, not a record of the real colours. We do not identify anyone, do not use photos to recognise or verify a person, and do not create biometric templates or face geometry. A photo can still identify the people in it, and the providers process the faces in it to produce the result you asked for.

Only send photos you have the right to use, with the permission of the people shown where it is required.

## How long photos are kept

- **Our server** does not store your photo or the result. For each job it keeps a record without the image (see below), including a SHA-256 fingerprint of the photo sent, which lets us recognise a repeated request.
- **fal.ai**: we ask fal.ai not to keep the request in its request history. The finished photo or video is kept in fal.ai storage for 7 days so the App can download it, and is then deleted. That period is a setting we choose.
- **OpenAI** states that data sent to its API is kept for up to 30 days in abuse-monitoring logs and is not used to train its models by default.
- **PixVerse** (only when you use Animate) does not publish a retention period for material processed this way, and we have not established one. This is the one link where we cannot give you a number.
- **On your phone**, a photo waiting to be sent is removed after it is processed, or after 24 hours if it was never sent (at most 7 days). Downloaded results stay in the App's private storage until you delete them or uninstall the App. History keeps up to 50 results; when it is full, the oldest are removed first, starting with ones you already saved to your gallery. Photos you save go to your gallery (Pictures/Restina or Movies/Restina) and stay there under your control. The App's data is excluded from Android backup.

## Other information

| What | Why | How long |
|---|---|---|
| A device identifier calculated by the App from Android's ID for this app (a one-way function: the App sends our server and analytics this identifier, not the Android ID itself; the Adapty SDK does send the Android ID to Adapty, see below). It usually stays the same if you reinstall the App on the same device. It is not the advertising ID. | to give the free photo once per device, keep your subscription working, enforce usage limits and group analytics events | the device record and the record that the free photo was used are kept while they are needed to prevent repeated free use; see deletion below |
| An installation key: a hash of the same Android ID | to limit free use and repeated security checks per device | stored only as a keyed hash in usage records |
| Job records: times, operation, status, error code, processing version, fal.ai request id, link to the result in fal.ai storage, consent version, photo fingerprint | to deliver your result and see when processing breaks | 90 days after the job ends |
| Usage counts and daily spending totals | to enforce daily and weekly limits and keep costs predictable | paid usage counts 30 days; daily totals 2 days; the record of the free photo – see above |
| Subscription records: product, status, expiry, Google Play transaction chain id, linked devices | to know whether your subscription is active and to stop one subscription being misused on other devices | not deleted automatically at present; removed on request, except what we must keep (see deletion below) |
| Your IP address, as seen by our server | on our server, only for rate limiting and abuse prevention, not for profiling. Mixpanel and Adapty also receive it, see the next section | rate-limit counters are removed automatically, usually within hours; Cloudflare's technical request logs for our server, which can include your IP address, are kept for up to 7 days |
| Google Play Integrity result | to check that requests come from a genuine copy of the App from Google Play | not stored in our database; our own log line has no token or IP address, and it sits in the request logs described above (up to 7 days) |
| Product analytics events (screens opened, whether a restoration succeeded, your rating of a result and the reason you pick, your answer on the photo permission, timings, subscription status) | to find where the App fails people | under Mixpanel's retention for our project |
| Crash reports | to fix crashes | under Firebase's retention |

We do not collect your name, email address, phone number, contacts or precise location. If you write to us, we receive whatever your email contains. The App's "Contact support" letter adds error codes, request ids, the App version, your language and your device identifier so we can find the problem; you see the letter before sending it.

## Services that process data

| Service | What it receives | What for |
|---|---|---|
| Cloudflare (our server hosting) | requests to our server, including IP address and the device identifier; technical request logs are kept for up to 7 days | hosting, delivery and protection |
| fal.ai (United States) | your photo and the result | runs the model request and stores the result for 7 days |
| OpenAI, through fal.ai (United States) | your photo and the edited result | restore, colourise, scratches, lighten |
| PixVerse, through fal.ai | your photo and the video made from it | Animate |
| Google Play | purchase and subscription details | payment; we never see your card |
| Adapty | subscription and purchase events, the device identifier (as the customer id), an analytics identifier, and what its SDK collects itself: IP address, the Android ID, the App Set ID, device model, OS, language, time zone and store country | subscription management, paywall and checking that a subscription belongs to this device |
| Mixpanel (EU data centre) | analytics events, the device identifier, approximate location derived from IP address, standard device and app properties | product analytics |
| Google Firebase Crashlytics | crash reports, device and app details, installation id | stability |
| Google Play Integrity | integrity token from Google Play | anti-abuse checks |

OpenAI and PixVerse receive your photo through fal.ai, and their own published terms govern what they then do with it. Our settings at fal.ai do not decide how OpenAI or PixVerse treat their copies. This is why our Google Play data safety section lists photos as shared.

Analytics and crash reporting start when the App opens. The photo permission covers sending photos only; it is not a switch for analytics. The App has no in-app switch to turn analytics off; uninstalling the App stops all collection. Analytics events do not contain your photos.

The App shows no ads, contains no advertising SDK and does not use the Android advertising ID. We do not sell your data or share it for advertising.

## Security and transfers

All connections from the App to our server and to these services use HTTPS. Results and pending photos are kept in the App's private storage, and identity, consent and pending-send records are excluded from backup. No method is perfectly secure.

Processing a photo means sending it outside the European Union: fal.ai, OpenAI and PixVerse process it in the United States. Mixpanel stores our analytics in its EU data centre; other services may process data in other countries.

<h2 id="delete-data">Deleting your data</h2>

This section applies to Restore Old Photos: Colorize (Restina) by Fablewood Studio.

In the App:

- Delete a result: open it and tap Delete. A copy you saved to your gallery stays.
- Stop sending photos: Menu → Sending photos → Withdraw permission.
- Uninstalling the App removes everything stored on your phone, except photos you saved to the gallery. It does not cancel a subscription: manage it in Google Play.

To ask us to delete data held on our server and by our services:

1. In the App, open Menu and tap the line "Version … · device …" at the bottom. This copies your device identifier.
2. Email [quicklysearch.bot@gmail.com](mailto:quicklysearch.bot@gmail.com) with the subject "Delete my data" and paste the identifier. Do not send photos, passwords or card details.
3. We delete the job records, usage records, device links and subscription links for that identifier, and ask Adapty and Mixpanel to delete their records linked to it. Crash reports in Firebase are not linked to this identifier, so we cannot find them by it; they expire under Firebase's retention. We reply when it is done, within 30 days.

What we may keep: a record that this device already used its free photo (without it, deletion would give a new free photo, so it is kept to prevent abuse), and purchase records that we or Google Play must keep for accounting, refunds or legal reasons. Results in fal.ai storage expire on their own after 7 days. Data already processed by OpenAI or PixVerse is subject to their own retention described above.

## Age, rights and changes

The App is intended for adults aged 18 and over and is not directed to children. We do not knowingly collect children's data.

If you are in the European Union or the United Kingdom, we rely on these lawful bases: performance of a contract, to process your photos and provide the subscription you ask for; your consent, for sending photos to the AI providers (you can withdraw it in the App); and our legitimate interests, for analytics, crash reports, fraud prevention and security. Analytics and crash reporting start when the App opens and have no separate consent screen; you can object by writing to us or stop them by uninstalling the App.

Depending on where you live, you may have the right to access, correct or delete your data, or to object to processing. Write to the address above. Because there is no account, we identify your data by the device identifier. You can also complain to your local data protection authority.

If this policy changes, we will update the effective date above and, if the change is significant, tell you in the App.

## Provider information

[OpenAI API data controls](https://developers.openai.com/api/docs/guides/your-data) · [fal.ai privacy](https://fal.ai/legal/privacy-policy) · [PixVerse privacy](https://pixverse.ai/en/privacy-policy) · [Mixpanel privacy](https://mixpanel.com/legal/privacy-policy/) · [Adapty privacy](https://adapty.io/privacy/) · [Firebase privacy](https://firebase.google.com/support/privacy/) · [Google privacy](https://policies.google.com/privacy) · [Cloudflare privacy](https://www.cloudflare.com/privacypolicy/)
