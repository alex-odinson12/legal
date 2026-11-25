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
| A device identifier calculated by the App from Android's ID for this app (a one-way function: the App sends this identifier, not the Android ID itself, to our server, Mixpanel and Adapty; the Adapty SDK does send the Android ID to Adapty, see below). It usually stays the same if you reinstall the App on the same device. It is not the advertising ID, and the App does not send it to Google Analytics. | to give the free photo once per device, keep your subscription working, enforce usage limits and group analytics events | the device record and the record that the free photo was used are kept while they are needed to prevent repeated free use; see deletion below |
| An installation key: a hash of the same Android ID | to limit free use and repeated security checks per device | stored only as a keyed hash in usage records |
| Job records: times, operation, status, error code, processing version, fal.ai request id, link to the result in fal.ai storage, consent version, photo fingerprint | to deliver your result and see when processing breaks | 90 days after the job ends |
| Usage counts and daily spending totals | to enforce daily and weekly limits and keep costs predictable | paid usage counts 30 days; daily totals 2 days; the record of the free photo – see above |
| Subscription records: product, status, expiry, Google Play transaction chain id, linked devices | to know whether your subscription is active and to stop one subscription being misused on other devices | not deleted automatically at present; removed on request, except what we must keep (see deletion below) |
| Your IP address, as seen by our server | on our server, only for rate limiting and abuse prevention, not for profiling. Mixpanel, Adapty and Google Analytics also receive it, see the next section | rate-limit counters are removed automatically, usually within hours; Cloudflare's technical request logs for our server, which can include your IP address, are kept for up to 7 days |
| Google Play Integrity result | to check that requests come from a genuine copy of the App from Google Play | not stored in our database; our own log line has no token or IP address, and it sits in the request logs described above (up to 7 days) |
| Product analytics events in Mixpanel (screens opened, whether a restoration succeeded, your rating of a result and the reason you pick, your answer on the photo permission, timings, subscription status) | to find where the App fails people | under Mixpanel's retention for our project |
| AI content reports you choose to send: a random report number, the reason you picked, where you opened the report (result, History, processing screen or Menu), whether it was a photo, a video or a general report from the Menu, the operation (such as Restore or Animate) and whether it was the previous result, the App language, platform, version, build number and build type (including whether it is a test build), and the time. A report does not contain your photo, the result, the device identifier or any other identifier of you; the report number is used in its place. | to review reports about harmful or offensive AI results and improve our safeguards (Google Play requires apps with AI-generated content to offer this) | under Mixpanel's retention for our project |
| Google Analytics data: your Android advertising ID (when available), a Firebase app instance ID for this installation, approximate location derived from your IP address, app and device details, how the App was installed (the install referrer from Google Play), Firebase's automatic events (such as first open, sessions and screen views) and two events of our own: the start of a free trial (with the plan) and a paid subscription purchase (plan, price and currency) | to see whether our ads in other apps and on websites lead to installs, trials and purchases | event-level data 2 months; user-level data 14 months from the installation's last activity; aggregated reports are kept longer |
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
| Adapty | subscription and purchase events, the device identifier (as the customer id), the Mixpanel identifier, and what its SDK collects itself: IP address, the Android ID, the App Set ID, device model, OS, language, time zone and store country. The App switches off Adapty's collection of the advertising ID, so Adapty does not receive it; Adapty does not receive the Firebase app instance ID either | subscription management, paywall and checking that a subscription belongs to this device |
| Mixpanel (EU data centre) | analytics events, the device identifier, approximate location derived from IP address, standard device and app properties | product analytics |
| Mixpanel (EU data centre), AI content reports | the AI content report described above, sent directly from the App with a random report number and without the device identifier; Mixpanel sees your IP address when receiving it, and the App asks Mixpanel not to use it for location | receiving and reviewing AI content reports |
| Google Analytics for Firebase (Google) | the Google Analytics data described in the previous section | measuring our advertising; see below |
| Google Firebase Crashlytics | crash reports, device and app details, installation id; with Google Analytics present, Crashlytics also records a crash event in Analytics and adds the Analytics events just before a crash to the report | stability |
| Google Play Integrity | integrity token from Google Play | anti-abuse checks |

OpenAI and PixVerse receive your photo through fal.ai, and their own published terms govern what they then do with it. Our settings at fal.ai do not decide how OpenAI or PixVerse treat their copies. This is why our Google Play data safety section lists photos as shared.

Analytics and crash reporting start when the App opens; Google Analytics collects only in the released version of the App, not in development builds. The photo permission covers sending photos only; it is not a switch for analytics. The App has no in-app switch to turn analytics off; uninstalling the App stops all collection. Analytics events do not contain your photos.

## Advertising measurement

The App shows no ads and contains no advertising SDK. We advertise the App elsewhere, for example through Google Ads, and use Google Analytics to see whether that advertising works. From the App, Google Analytics receives Firebase's automatic events (in-app purchase events only if Google Play is linked to Firebase) and only two events of our own, both about subscriptions: the start of a free trial (with the plan) and a paid subscription purchase (plan, price and currency). When a Google Play test account makes a purchase, these two events go under separate test names, and we do not count them as ad results; Firebase's automatic events are not renamed. The App does not send Google Analytics your photos, the device identifier or a user ID, and sets no user properties. Google signals is turned off in our Analytics property.

We link or may link Google Analytics to Google Ads, so Google can match installs, trials and purchases to our ad campaigns, report the results to us and optimise the campaigns. When this link is active, we share these identifiers, events, purchase information and approximate location with Google for advertising. Google Analytics processes data on our behalf; once data is used in Google Ads, Google also uses it for its own purposes under its terms, for example to improve its advertising systems. We do not sell your data for money. More details: [how Google uses data from apps that use its services](https://policies.google.com/technologies/partner-sites).

For users in the European Economic Area, the United Kingdom and Switzerland, the App tells Google Analytics by default that consent is not given for sending personal data to Google for advertising (ad_user_data) or for ad personalisation (ad_personalization). Analytics collection continues. The App does not show a consent screen, and analytics storage and ad storage are not switched off for anyone.

You control the advertising ID yourself: in Android Settings open Security & privacy, then Privacy, then Ads (the exact path depends on your device), where you can reset or delete it. After you delete it, the App and its SDKs receive no advertising ID, and the other data described here is still processed.

The App's manifest includes permissions that come with Google Analytics for Firebase, including the Google Play advertising ID permission (com.google.android.gms.permission.AD_ID) and the Android Privacy Sandbox attribution permissions (ACCESS_ADSERVICES_ATTRIBUTION and ACCESS_ADSERVICES_AD_ID).

## Security and transfers

All connections from the App to our server and to these services use HTTPS. Results and pending photos are kept in the App's private storage, and identity, consent and pending-send records are excluded from backup. No method is perfectly secure.

Processing a photo means sending it outside the European Union: fal.ai, OpenAI and PixVerse process it in the United States. Mixpanel stores our analytics in its EU data centre; other services may process data in other countries.

<h2 id="delete-data">Deleting your data</h2>

This section applies to Restore Old Photos: Colorize (Restina) by Fablewood Studio.

In the App:

- Delete a result: open it and tap Delete. A copy you saved to your gallery stays.
- Stop sending photos: Menu → Sending photos → Withdraw permission.
- Uninstalling the App removes everything stored on your phone, except photos you saved to the gallery. It does not cancel a subscription: manage it in Google Play.

AI content reports are not linked to the device identifier, so the steps below do not find them. To have a report deleted, email [quicklysearch.bot@gmail.com](mailto:quicklysearch.bot@gmail.com) with the subject "Delete my AI content report" and only the report number shown in the App. You do not need to send the device identifier for this.

To ask us to delete data linked to your device on our server and at our services:

1. In the App, open Menu and tap the line "Version … · device …" at the bottom. This copies your device identifier.
2. Email [quicklysearch.bot@gmail.com](mailto:quicklysearch.bot@gmail.com) with the subject "Delete my data" and paste the identifier. Do not send photos, passwords or card details.
3. We delete the job records, usage records, device links and subscription links for that identifier, and ask Adapty and Mixpanel to delete their records linked to it. Crash reports in Firebase are not linked to this identifier, so we cannot find them by it; they expire under Firebase's retention. Google Analytics data is not linked to it either, so we cannot find it by it; it expires after the periods given above. Deleting your data does not reset your advertising ID: you do that in Android Settings (see above). We reply when it is done, within 30 days.

What we may keep: a record that this device already used its free photo (without it, deletion would give a new free photo, so it is kept to prevent abuse), and purchase records that we or Google Play must keep for accounting, refunds or legal reasons. Results in fal.ai storage expire on their own after 7 days. Data already processed by OpenAI or PixVerse is subject to their own retention described above.

## Age, rights and changes

The App is intended for adults aged 18 and over and is not directed to children. We do not knowingly collect children's data.

If you are in the European Union or the United Kingdom, we rely on these lawful bases: performance of a contract, to process your photos and provide the subscription you ask for; your consent, for sending photos to the AI providers (you can withdraw it in the App); and our legitimate interests, for analytics, measuring our advertising, crash reports, fraud prevention and security. Analytics and crash reporting start when the App opens and have no separate consent screen; you can object by writing to us or stop them by uninstalling the App. In these regions the App tells Google by default that consent for advertising use is not given (see Advertising measurement).

Depending on where you live, you may have the right to access, correct or delete your data, or to object to processing. Write to the address above. Because there is no account, we identify your data by the device identifier, and an AI content report by its report number. You can also complain to your local data protection authority.

If this policy changes, we will update the effective date above and, if the change is significant, tell you in the App.

## Provider information

[OpenAI API data controls](https://developers.openai.com/api/docs/guides/your-data) · [fal.ai privacy](https://fal.ai/legal/privacy-policy) · [PixVerse privacy](https://pixverse.ai/en/privacy-policy) · [Mixpanel privacy](https://mixpanel.com/legal/privacy-policy/) · [Adapty privacy](https://adapty.io/privacy/) · [Firebase privacy](https://firebase.google.com/support/privacy/) · [Google Analytics for Firebase data](https://support.google.com/analytics/answer/11582702) · [Google privacy](https://policies.google.com/privacy) · [Google partner sites and apps](https://policies.google.com/technologies/partner-sites) · [Cloudflare privacy](https://www.cloudflare.com/privacypolicy/)
