Sudan P2P Tracker 🇸🇩

Automated Binance P2P USDT/SDG Price Tracker

Created and maintained by JinRal-dev.

An open-source project for monitoring public Binance P2P USDT/SDG advertisements, with a focus on Bank of Khartoum payment methods.

Features

* Fetches public Binance P2P BUY advertisements for USDT/SDG.
* Filters advertisements by Bank of Khartoum.
* Records prices, available USDT, advertiser names, and seller statistics.
* Saves the latest results to prices.json.
* Uses GitHub Actions for automated updates every 6 hours.
* Publishes the JSON data through GitHub Pages.
* Supports optional synchronization to Google Drive using Google Apps Script.

Live Data

View latest published prices

The JSON contains:

* source — Data provider
* pair — Currency pair
* side — BUY or SELL
* payment_method — Payment method filter
* updated_at_utc — Time of the last successful fetch
* offers — Public P2P advertisements and advertiser statistics

Advertisement limits are stored as raw values because their units require further verification.

Quick Start

1. Fork this repository to your GitHub account.
2. Review tracker.py and adjust the asset, fiat currency, or payment-method filters if necessary.
3. Enable GitHub Actions for your fork.
4. Run the Update Binance P2P Prices workflow manually to test it.
5. Confirm that prices.json has been generated.
6. Allow the scheduled workflow to run automatically.

The workflow requires permission to write repository contents.

Automation

The workflow is located at:

.github/workflows/update.yml

It is configured to run every 6 hours and can also be triggered manually.

Scheduled GitHub Actions may experience delays. Binance may change or restrict its public endpoints without notice.

Google Drive Integration (Optional)

You can use Google Apps Script to periodically fetch the published prices.json file and synchronize it to a Google Drive folder.

Create your own Apps Script project, configure your own Drive folder ID, and use a time-driven trigger. Do not reuse another person’s private folder ID or share Google credentials.

Important Disclaimer

* This project reads publicly displayed advertisements only.
* It does not execute trades, access Binance balances, or require Binance API keys.
* Advertised prices are not guaranteed executable prices.
* Seller statistics and available quantities may change.
* Transaction-limit units should be independently verified before making purchasing decisions.
* This project is not affiliated with Binance or Bank of Khartoum.
* Users should comply with applicable laws and platform terms.

⸻

النسخة العربية 🇸🇩

متتبع أسعار Binance P2P في السودان

مشروع مفتوح المصدر أنشأه JinRal-dev لمتابعة إعلانات شراء USDT مقابل الجنيه السوداني، مع التركيز على التحويل عبر بنك الخرطوم.

ماذا يفعل المشروع؟

* يجلب إعلانات Binance P2P العامة.
* يعرض أسعار شراء USDT مقابل الجنيه السوداني.
* يرشّح الإعلانات التي تدعم بنك الخرطوم.
* يحفظ بيانات التجار ونسب إكمال الطلبات والكميات المعروضة.
* يحدث البيانات تلقائيًا كل 6 ساعات باستخدام GitHub Actions.
* ينشر النتائج بصيغة JSON.
* يمكن ربطه اختياريًا بـ Google Drive.

كيفية الاستخدام

1. افتح المشروع على GitHub.
2. أنشئ نسخة باستخدام Fork.
3. فعّل GitHub Actions.
4. شغّل Workflow يدويًا للاختبار.
5. تأكد من إنشاء ملف prices.json.
6. اترك التحديثات المجدولة تعمل تلقائيًا.

رابط البيانات

عرض أحدث الأسعار المنشورة

ملاحظات مهمة

الأسعار تمثل إعلانات منشورة وليست صفقات منفذة أو أسعارًا مضمونة. يجب التحقق من حدود المعاملات وصلاحية الإعلان قبل أي عملية شراء.

المشروع لا يحتاج إلى بيانات تسجيل دخول Binance، ولا ينفذ أي معاملات مالية.

Project by JinRal-dev — Sudan 🇸🇩
