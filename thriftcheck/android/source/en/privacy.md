# Privacy Policy for ThriftCheck: Vintage Resale AI

Effective date: {{EFFECTIVE_DATE}}. Android app, package com.thriftcheck.scanner.

## Who we are

Fablewood Studio publishes ThriftCheck: Vintage Resale AI (also shown as ThriftCheck) on Google Play (the App). In this policy "we" and "us" mean the developer of the App. For privacy questions or a data request, write to [quicklysearch.bot@gmail.com](mailto:quicklysearch.bot@gmail.com).

The App estimates what a second-hand item is and what it could resell for, from photos you take of it. This page explains what the App collects, who receives it and how long it is kept. It covers the Android app only. There is no account and no registration: we do not ask for your name, email address, phone number or password. The App shows no ads.

## Photos you send

You take the photos with the camera inside the App or pick them with the Android photo picker. The App does not browse your photo library and does not ask for permission to read your storage. It asks for camera permission the first time you choose the camera; without it, the photo picker still works.

When the App starts, it asks our server whether the service is available in your country. Before it offers the free check, it also asks whether this device can still get it. These requests carry the device identifier, the Adapty profile identifier, the App version and a request identifier; the free check question also carries a Google Play Integrity token.

When you tap Analyze, the App sends to our server:

- **one to three photos**, prepared for sending: the App decodes each photo into pixels and writes a new JPEG file with the longer side at most 1024 pixels. Because the file is rebuilt from pixels, the location and camera details stored inside the original photo are not copied into it;
- **the category** you chose and **the App's language**, so the answer comes back in your language;
- **a device identifier, an Adapty profile identifier, the App version, a request identifier and a Google Play Integrity token** (see "Identifiers" below).

The request travels over HTTPS to our server, which runs on Vercel in the United States. Our server passes the photos, the category and the language to **OpenAI**, whose model identifies the item and estimates its condition and value. OpenAI does not receive the device identifier, the profile identifier or anything else about you. The model receives the whole picture, so anything else in the frame (a face, a document, a room) goes with it. Frame the item, not your surroundings.

Our server does not save the photos. It keeps the AI result (item name, brand, era, condition, price range, verdict and notes) for a limited time, so that a repeated request is not charged twice, so that price estimates can be produced for it and so that you can report a wrong result. The periods are in "What our server keeps" below.

**OpenAI's retention.** This describes OpenAI's system, not ours. According to OpenAI's API data page (checked 14 November 2026), data sent through the API is not used to train OpenAI's models by default, and OpenAI keeps it for up to 30 days in abuse-monitoring logs unless the law requires longer. OpenAI also says that an image its safety systems flag as possible child sexual abuse material is kept for manual review. We do not control what OpenAI keeps.

## Market price estimates

When the result of a new scan is shown, the App asks our server for market price estimates. Our server builds this request itself from the stored AI result: item name, brand, era, condition and category. It sends that text to **Perplexity**, whose AI searches the web for prices on eBay, Mercari, Poshmark and Etsy. The App sends no text of yours for this, and no photo or identifier reaches Perplexity.

**Perplexity's retention.** Perplexity states that it does not use customer content to train generative AI models. Its API documentation (privacy and security page, checked 14 November 2026) says that retention depends on the API, model and account configuration and that zero data retention is not the default. We have not established a retention period for these requests; Perplexity's API terms govern what it keeps.

These prices are AI estimates found by web search, not data supplied by the marketplaces.

## Identifiers

| Identifier | What it is | Who receives it | Why |
|---|---|---|---|
| Device identifier | the Android ID that Android gives this app on this device and user; if it is missing or invalid, a random installation ID created by the App | our server. The App does not give it to Mixpanel or Crashlytics. The Adapty library reads the Android ID on its own and sends it to Adapty (see below) | one free check per device, daily limits, fraud prevention |
| Adapty profile ID | a random ID created by the Adapty library on first start | Adapty and our server | checking whether your subscription is active, and the limit of 3 devices per subscription (see the Terms of Use) |
| Mixpanel ID | a random ID created by the Mixpanel library | Mixpanel; the App also gives it to Adapty, so subscription events can be matched to analytics | analytics |
| Firebase installation ID | created by Firebase | Google (Firebase Crashlytics) | crash reports |
| Data the Adapty library collects itself | the Android ID, the App Set ID (an ID shared by apps of one developer on a device), the Google Play install referrer (how the App was installed), its own installation and session IDs, device model and display details, Android version, language, time zone, store country, and its own events about App use (for example when the App is opened) and about the library's work | Adapty | subscriptions, subscription analytics and the library's diagnostics |
| Data the Firebase libraries collect themselves | session IDs and start times, the Firebase installation ID, App version, Android version, device model and manufacturer | Google (Firebase) | App stability; sent when App sessions start, also when nothing crashes |

**Our server never stores the device identifier, the profile ID or your IP address in readable form.** Before anything is written, each one is turned into a keyed hash (HMAC-SHA256), each with its own secret key. The same input always gives the same hash, which is what makes limits work, so these hashes are pseudonyms, not anonymous data: someone holding both our database and our keys could check whether a given device or profile is in it.

**Google Play Integrity.** Before a scan, a price estimate and a report, and before the free check is offered, the App asks Google Play for an integrity token and sends it to our server (or an error code, if Google Play cannot provide one). Our server asks Google to decode the token. The answer tells us whether the request comes from a genuine copy of the App installed from Google Play on a genuine device. Google processes this under its own terms.

The App does not use the Android advertising ID: the advertising ID permission is removed from the App, the library that reads it is left out of the build, and Adapty is told not to collect it.

## Your IP address and country

Every internet request carries your IP address. This is what happens to it.

- **Country.** Vercel, which hosts our server, tells our server which country the request comes from (for Ukraine, also the region), based on the IP address. We use it to refuse service where OpenAI does not allow its service to be used (see the Terms of Use). The country code is written to our server logs and stored with a report. The App does not ask for your device location.
- **The free check.** When you use the free check, our server turns your IP address (for IPv6, its /64 network) into a keyed hash and counts free-check requests per day against it. The hash is the same every day.
- **Everywhere else** our server does not write your IP address or its hash, and our logs do not contain it.
- **Our providers.** Vercel receives your IP address with every request to our server and may record it in its own logs and protection systems. Mixpanel and Adapty receive it when the App connects to them. The App tells Mixpanel not to work out your location from the IP address, and tells Adapty not to collect the IP address. Google receives it for Play services and crash reports.

## Reporting an AI result

Each result has a "Report AI result" button with four reasons and no text field. The report goes to our server with the scan's request ID, the reason, the device and profile identifiers (stored only as hashes), the App version and a Google Play Integrity token; our server adds your country. If Google Play confirms the device and the report comes from the device and profile that made the scan while its AI result is still stored (7 days), our server attaches a copy of that result, so that we can see what the model said. Without a connection, or when the daily limit is reached, the App keeps the report and sends it later, even if you delete the scan from your history in the meantime.

If you report by email instead, or use "Contact Developer", the App opens your mail app with a prepared message: the check number shown on the result and the reason, or the App version, plus the last 6 characters of your profile ID. You see the message before sending it. We receive your email address and whatever you write. Our mailbox is Gmail, provided by Google.

## What stays on your phone

| What | Notes |
|---|---|
| Scan history: the 50 most recent scans, each with a copy of the main photo (longer side up to 1600 pixels), the AI result, the price estimates and the purchase price you typed into the profit calculator | deleting a scan, or clearing the history, deletes its photo too |
| An unfinished scan: the prepared photos, the request with your identifiers, and the result if it arrived but was not yet saved to history | so that a scan interrupted by a crash or a lost connection can be finished without paying again; deleted when the scan is finished or can no longer be finished; the record of a failed attempt is kept for about a day after it can no longer be retried. The App checks this when you next use it, so a scan left unfinished stays until then |
| Photos you have taken or picked but not yet analyzed | temporary copies in the App's cache |
| Reports waiting to be sent | the request ID and the reason, until the report is sent or refused. A report sent without Google Play's confirmation of the device is kept for up to 30 days to send that confirmation later |
| Settings: onboarding progress, your survey answers, the installation ID, whether the free check was used, the last region answer (used for up to 7 days offline) | App preferences |
| PDF reports and photos you share | copies in the App's cache; deleting the scan from history does not delete these copies. The app you share them with receives the PDF (check number, photo, AI result, prices and, if you entered it, your purchase price) or the photo and text, and keeps them under its own rules |

All of this is in the App's private storage. **None of it is backed up:** the App turns off Android backup and excludes all of its data from cloud backup and device-to-device transfer, so a new phone starts with an empty history. Uninstalling the App deletes all of it. It does not delete what is held on our server or by the companies listed below.

## Analytics

The App sends usage events to **Mixpanel**, to its EU data centre: screens and onboarding steps, survey answers, categories chosen, scans started and their outcome (verdict, confidence, error type), price estimate requests, paywall views, purchase outcomes, restore attempts, history actions and menu taps. Each event carries the App version and build, Android version, your phone's language and region settings (from the phone's settings, not from your location), the number of App launches, days since first launch and, on some events, whether you have a subscription. Your survey answers are also attached to later events. The Mixpanel library adds technical properties itself, such as device model, manufacturer, operating system version, screen size and network type.

Some events carry more than counts:

- **the onboarding survey** asks what you use the App for and where you shop. If you choose "Other", you can type up to 100 characters; that text is sent to Mixpanel and saved on your Mixpanel profile. Do not type anything personal there. Survey answers are used only to improve the App; they do not change the prices or verdicts you see;
- **the region check** event carries whether the service is available where you are (as decided by our server from your IP address) and whether the free check is still available;
- **the profit calculator** events carry the purchase price you typed, the margin and return calculated from it, and the AI's and the recalculated verdict;
- **sharing** events carry the format, the verdict, confidence and category, the time taken and the file size;
- **"See sold on eBay"** carries the item name found by the AI;
- **a purchase** event carries the product, price and currency;
- **a report** event carries the reason, the check number shown on the result, the category and the verdicts.

Your Mixpanel profile also records whether you used the free check and how many analyses you ran. The App gives Adapty your Mixpanel ID so that Adapty can send subscription events (such as trial starts, renewals and cancellations, with price) to Mixpanel for the same user.

Analytics events do not contain your photos, the AI's explanations, the device identifier, the profile ID or the text you type into the history search (only its length). Analytics start when the App opens. There is no in-app switch to turn them off; uninstalling the App stops collection by the App.

## Crash reports

The App uses **Firebase Crashlytics** (Google) for crash reports and for reports of some errors. Crashlytics receives the error, device and App details and the Firebase installation ID. Google states that it keeps crash reports and their identifiers for 90 days. The App does not give Crashlytics the device identifier or the profile ID, but an error message can include the internal ID of a scan stored on your phone. The Firebase libraries also send session data, also when nothing crashes (see "Identifiers"). The App does not include Google Analytics for Firebase.

## Subscriptions and payments

Subscriptions are sold through **Google Play Billing**. Google processes the payment; we never see your card or payment details. The **Adapty** library in the App receives your subscription status and purchase history from Google Play and manages access to premium features. Our server asks Adapty, by profile ID, whether your subscription is active.

## Who receives data

| Company | What it receives | Why |
|---|---|---|
| OpenAI (United States) | the photos you analyze, the category, the language | identifying the item and estimating its value |
| Perplexity (United States) | item name, brand, era, condition and category from the AI result | market price estimates |
| Vercel (United States) | every request to our server, including your IP address | hosting our server |
| Neon (United States) | everything our server stores (see "What our server keeps") | hosting our database |
| Google | Play Billing purchases; Play Integrity tokens; crash reports, session data and the Firebase installation ID (Crashlytics); emails you send us (Gmail) | payments, fraud prevention, App stability, support |
| Adapty | profile ID, subscription status and purchase history, the Mixpanel ID, and what its library collects itself (see "Identifiers") | subscriptions |
| Mixpanel (EU data centre) | usage events and survey answers (see "Analytics"), and subscription events if Adapty sends them | analytics |
| eBay, Mercari, Poshmark, Etsy | only when you tap a link: "See sold on eBay" opens an eBay search for the item name and brand, and a price source opens the marketplace page in your browser | showing you listings |

Each company keeps what it receives under its own retention rules and our account settings with it. We do not sell your data and do not share it for advertising. The App does not track you across other companies' apps or websites.

## What our server keeps, and for how long

A daily job, in place since 14 November 2026, deletes these records automatically. A record becomes due at the end of the period below and is normally removed by the next daily run, so it can stay up to about one day longer. A failed or overloaded run, or a request still being processed, can delay removal until a later run. The job covers only our own database: data held by our providers, logs and emails are not deleted by it.

| What we store | Why | How long |
|---|---|---|
| The AI result of a scan, with the hashed device and profile identifiers, the category and the type of access (subscription or free check) | answering a retry without charging twice, price estimates, reports | 7 days from the start of the scan |
| A technical record of the scan, after the result is removed: request ID, status, a hash of the request, the error answer if the scan failed, times, number of attempts, and a keyed tag derived from the hashed identifiers that lets us confirm the scan belonged to a device | recognising repeated requests and answering that the result has expired | until 90 days after the start of the scan (about 83 days after the result is removed) |
| Price estimates for a scan | answering a retry without charging twice | 7 days from the first price request |
| Reports on AI results, with the copy of the AI result where one was attached | reviewing wrong or harmful AI output | 30 days from the report. A copy is attached only while the result is still stored, so it can stay up to about 37 days after the scan |
| The free check record of a device: hashed device identifier, status (available, reserved or used), the request ID of the scan, the number of failed attempts and times. It is created when the device first tries the free check, whether or not that succeeds | one free check per device | **kept indefinitely**: deleting it would give the device a new free check |
| The link between a hashed profile ID and the hashed devices that used it | the limit of 3 devices per subscription | 30 days after the device was last seen. An internal marker per hashed profile ID, used to handle its requests one at a time, is deleted when the profile has no such link left |
| Subscription state: hashed profile ID, expiry date and when we last checked it with Adapty | serving a subscriber while Adapty is briefly unavailable | until 72 hours after the subscription expires or 7 days after our last check, whichever is later; 7 days after the last check if there is no expiry date |
| Daily counters per hashed device, hashed profile and, for the free check, hashed IP address; counters of price estimates and reports | usage limits | about 41 to 42 days after the day counted (days in UTC) |
| Records of AI costs per request (request ID, amounts, no device or profile identifier) and daily and monthly totals | spending limits | 40 days from creation; totals 40 days after their last update |

Our server logs record, for each request, operational and security details: the route, the result code, a short hash of the request ID, the country code, timing, the Play Integrity verdict, whether the free check was available, the number of AI tokens used and spending decisions. They do not contain your IP address, the device identifier, the profile ID, the photos or the AI's answer. Vercel keeps these logs under its own terms.

## Security

All connections from the App use HTTPS, and the App does not allow unencrypted connections. The keys for OpenAI and Perplexity are kept on our server, not in the App. On our server, device and profile identifiers and IP addresses are stored only as keyed hashes. Our server reaches the database through a role that can only run our own database functions, not read tables directly. No method is perfectly secure.

## Legal bases and international transfers

Where data protection laws such as the GDPR apply, we rely on these legal bases: **performance of a contract**, for the analysis, price estimates and subscription you ask for; **legitimate interests**, for fraud prevention, usage limits, the region restriction, security, crash reports and product analytics. Analytics and crash reporting have no separate consent screen; you can object by writing to us or stop them by uninstalling the App.

Our server and database run in the United States, and OpenAI and Perplexity process data there. Mixpanel stores our analytics in its EU data centre. Adapty and Google may process data in other countries.

<h2 id="delete-data">Your choices and deleting your data</h2>

This section applies to ThriftCheck: Vintage Resale AI by Fablewood Studio.

- **Camera.** You can refuse camera access and use the photo picker instead.
- **Survey.** Every survey question can be skipped.
- **On your phone.** Delete single scans, clear the history, or uninstall the App.
- **Subscription.** Manage or cancel it in Google Play (see the Terms of Use). Uninstalling the App does not cancel it.

To ask us to delete data held on our server and by our providers:

1. In the App, open **Settings** and **long-press the ID** at the bottom. This copies your full profile ID.
2. Email it to [quicklysearch.bot@gmail.com](mailto:quicklysearch.bot@gmail.com) with the subject "Delete my data", and say what you want. Do not send photos, passwords or card details.
3. We delete the records we can link to that profile ID and to the devices it was used with a subscription, and ask Adapty and Mixpanel to delete their records linked to it. We reply when it is done, within 30 days.

What we may keep: the mark that a device used its free check (without it, deletion would give a new free check); purchase records that we or Google Play must keep for accounting, refunds or legal reasons; and records that we cannot link to your profile ID, such as daily counters by hashed IP address or reports from a device never used with a subscription, which expire on their own (see above). Crash reports are not linked to the profile ID, so we cannot find them by it; Google keeps them for 90 days before deleting them. Data already processed by OpenAI or Perplexity is subject to their own retention described above. Support emails stay in our mailbox until we delete them; you can ask us to.

Treat the full profile ID like a password: anyone who has it can try to use your subscription on their own device. Send it only to the address above.

Depending on where you live, you may also have the right to access or correct your data, or to object to processing. Write to the address above. Because there is no account, we identify your data by the profile ID. You can also complain to your local data protection authority.

## Children

The App is intended for adults aged 18 and over and is not directed to children. It shows no ads. We do not knowingly collect children's data. If you believe a child has used the App, write to us and we will delete what we can identify.

## Changes to this policy

If we change how the App handles data, we will update this page and the effective date above and, if the change is significant, tell you in the App or in its Google Play release notes.

## Provider information

[OpenAI API data controls](https://developers.openai.com/api/docs/guides/your-data) · [Perplexity API privacy and security](https://docs.perplexity.ai/docs/resources/privacy-security) · [Mixpanel privacy](https://mixpanel.com/legal/privacy-policy/) · [Adapty privacy](https://adapty.io/privacy/) · [Firebase privacy and data retention](https://firebase.google.com/support/privacy/) · [Google privacy](https://policies.google.com/privacy) · [Vercel privacy](https://vercel.com/legal/privacy-notice) · [Neon privacy](https://neon.com/privacy-policy)
