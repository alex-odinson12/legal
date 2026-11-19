# Privacy Policy for AI Ethnicity: Face Scanner

Effective date: {{EFFECTIVE_DATE}}. Android package: com.heritageface.scanner.

## Who operates the app

Fablewood Studio operates AI Ethnicity: Face Scanner (the App). For privacy questions or a data request, contact [quicklysearch.bot@gmail.com](mailto:quicklysearch.bot@gmail.com).

The App creates fictional heritage stories and artistic AI images for entertainment. Its ethnicity percentages, appearance descriptions and partner profiles are generated content, not verified facts about you, DNA results or medical findings.

## Photos, information you enter and generated results

When you select a photo and continue with AI analysis, the App sends a compressed copy through our processing server to an AI provider. It also sends the first name and birthplace you provide, an age group and the selected onboarding answers. AI requests use an age group rather than your exact birth date. You can skip the name and birthplace questions. A photo is required for the core face-analysis feature.

Name analysis sends the first name and surname you choose, optional birthplace and relevant generated heritage information. Partner stories and historical portraits also use information from the generated report, including its fictional ethnicity, appearance and gender descriptions. Portrait generation uses text prompts; the current portrait requests do not include your original selfie.

Results and selected photos are saved in the App's private storage so you can return to them. The history normally keeps up to 20 reports. Generated heritage is sent for further processing when you request related AI features; it is not confined to local storage in those cases.

## Services that process data

- Our proxy runs on Vercel. It forwards AI requests. Our own quota database on Neon records installation identifiers, IP addresses, request dates, routes and counters to limit abuse and costs. That quota database is not used to store selfies or report content.
- OpenAI processes photo analysis and text requests, and can generate portraits as a fallback. Anthropic is a fallback route for photo analysis when available.
- fal.ai processes portrait text through a Google image model and hosts generated image files for download.
- Google Play Integrity checks that requests come from a genuine copy of the App on a genuine Android device. The App asks Google for an integrity verdict tied to the request and passes it to our proxy to limit abuse; Google processes device and app information for this check.
- Mixpanel processes usage events and pseudonymous profiles in its EU project. Events describe navigation, selected options, feature use, success/failure, timing and subscription status. They use a persistent identifier. Our analytics events do not attach your selfie or the name/birthplace text you entered. IP-based approximate location and standard app/device properties may be added by the SDK/service. These records are pseudonymous, not anonymous.
- Reports about AI content. If you choose to report a result, the App sends one event to our Mixpanel EU project with: a report ID, the reason you selected, the section and kind of content (text or portrait), the internal ID of the result and, for a time portrait, the era when applicable, the app language and build, and the same Mixpanel identifier as other events. Photos, result text, names and birth details are not sent. We use reports to review results and improve how they are generated. A report that could not be sent is not stored on the device.
- Adapty and Google Play process subscription status, product and transaction information, purchase history and identifiers used to validate or restore access. The Mixpanel identifier and the Firebase app instance ID are passed to Adapty as integration identifiers. The App switches off Adapty's collection of the Android advertising ID, so Adapty does not receive it. Adapty sends subscription events (for example, trial starts, a trial turning into a paid plan, renewals, cancellations, expirations and refunds) from its servers to Firebase, matched through the Firebase app instance ID. Automatic server-to-server forwarding from Adapty to Mixpanel is currently inactive; the App sends its own events to Mixpanel directly. We do not receive your full payment-card details.
- Firebase Crashlytics, Installations and Sessions process crash/nonfatal information, app/device metadata, session information and installation identifiers to diagnose stability problems. The App does not explicitly attach your photo or profile text to crash reports.
- Google Analytics for Firebase (Google LLC) processes usage and purchase events, your Android advertising ID (when available), a Firebase app instance ID that identifies this installation, approximate location derived from the IP address, and app and device information. From the App, Analytics receives Firebase's automatic events (such as first open, sessions and screen views; in-app purchase events only if Google Play is linked to Firebase) and only two events of our own, both about purchases: the start of a free trial (with the plan) and a paid subscription purchase (plan, amount, currency). When Google Play testers make purchases, these two events are sent under separate test names; Firebase's automatic events and Adapty's server events for such purchases are not renamed. Photos, names, birth dates and analysis results are not sent to Analytics. It collects only in the released version of the App, not in development builds. We use this data for analytics and to measure how well our advertising works. Subscription events from Adapty (see above) are added to the same Analytics property. We link or may link Firebase to Google Ads, so Google can match installs, trial starts and purchases to our ad campaigns, report conversions to us and optimize our campaigns. When this link is active, we share these identifiers, events, purchase information and approximate location with Google for advertising. Google Analytics processes data on our behalf; once data is used in Google Ads, Google also uses it for its own purposes under its terms, for example to improve its advertising systems. More details: [how Google uses data from apps that use its services](https://policies.google.com/technologies/partner-sites).

Analytics and diagnostics start when the App starts, before the separate AI-photo consent. That AI consent controls photo processing; it is not a switch for all SDK collection. The App does not display ads or include Facebook's SDK. We use advertising measurement for our own ads shown elsewhere; nothing in the App is an ad, and we do not sell your data for money. For users in the European Economic Area, the United Kingdom and Switzerland, the App tells Google Analytics by default that consent is not given for sending personal data to Google for advertising (ad_user_data) or for ad personalization (ad_personalization); analytics collection continues. The App does not show a consent screen, and analytics storage and ad storage are not switched off for anyone.

## Retention

App-private reports and photos remain until replaced by the history limit, removed through Reset All Data, or removed with the App. Temporary files can remain until reset, system cache cleanup or uninstall. Originals in your photo library and copies you export are separate.

Our proxy code forwards AI content without intentionally writing it to a permanent content store. This does not mean providers erase all inputs and outputs immediately. Their API processing, safety logs, generated-media hosting, legal exceptions and account settings have their own retention rules. OpenAI and Anthropic publish API retention information; fal hosts generated files under its media-retention terms. We do not promise Zero Data Retention.

Quota records are periodically pruned for abuse prevention. The current cleanup does not establish a guaranteed seven-day maximum. Hosting/security logs and backups can have separate retention. Mixpanel and Adapty records remain subject to their service settings and deletion processes. Firebase publishes retention for Crashlytics diagnostics and identifiers. In our Analytics property, Google Analytics keeps event-level data for 2 months and user-level data for 14 months, extended while the installation stays active; aggregated reports are kept longer.

## Reset, uninstall and deletion requests

Reset All Data removes the local profile, reports, private photo/portrait files, prepared share PDFs and AI-photo consent. It does not cancel a subscription, erase provider-side analytics (including Google Analytics) or purchase records, reset your advertising ID, reset the installation identifier or its abuse/trial counters, or delete files already saved to your gallery or another app.

Uninstalling removes the App's private local data through Android. It does not cancel Google Play billing or delete remote service records. You manage subscriptions through Google Play.

You control the advertising ID yourself: in Android Settings open Security & privacy, then Privacy, then Ads (the exact path depends on your device), where you can reset the ID or delete it. After you delete it, the App and its SDKs receive no advertising ID, and the other data described here is still processed.

You may request information, correction or deletion by emailing the address above. Because many records use pseudonymous service or installation identifiers rather than an email account, we may need limited information to locate and verify the relevant records. Do not send passwords, card details or an unsolicited selfie. Some records may need to be retained for security, transaction, legal or dispute-handling reasons. A local reset is not a remote deletion request.

## Permissions, security and transfers

The App uses Android's photo picker and system camera so you choose which photo to provide. It does not request broad camera or photo-library access for those actions. Saving images on older Android versions can require storage permission. The App does not request precise GPS location. The released App's manifest includes permissions that come with Firebase, including the Google Play advertising ID permission (com.google.android.gms.permission.AD_ID), and the Android Privacy Sandbox attribution permissions (ACCESS_ADSERVICES_ATTRIBUTION and ACCESS_ADSERVICES_AD_ID). They are added by Google Analytics for Firebase, which uses the advertising ID as described above for ad measurement.

Connections to our server and service endpoints use HTTPS. Access to service systems is restricted. No storage or transmission method can guarantee absolute security. Data may be processed outside your country by the providers and their subprocessors; using a Mixpanel EU project does not mean all AI, billing and diagnostic processing takes place in the EU.

If you export a report or image, the recipient you choose handles its copy under its own practices. Resetting the App cannot recall that copy.

## Children, rights and updates

The App is not designed for children under 13. Do not submit another person's image or information without the necessary permission. Applicable rights, including access, correction, deletion or objection to processing, depend on your location; contact us to make a request.

We will update this policy when our practices change. The published policy will show its effective date.

## Provider information

[OpenAI API data controls](https://developers.openai.com/api/docs/guides/your-data) · [Anthropic commercial retention](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data) · [fal API terms](https://fal.ai/legal/api-services) · [fal privacy](https://fal.ai/legal/privacy-policy) · [Mixpanel privacy](https://mixpanel.com/legal/privacy-policy/) · [Adapty privacy](https://adapty.io/privacy/) · [Firebase privacy](https://firebase.google.com/support/privacy/) · [Google Analytics for Firebase data](https://support.google.com/analytics/answer/11582702) · [Google privacy](https://policies.google.com/privacy) · [Google partner sites and apps](https://policies.google.com/technologies/partner-sites)
