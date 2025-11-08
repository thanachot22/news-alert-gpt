# 📰 News Alert GPT

ระบบวิเคราะห์ข่าวการเงินอัตโนมัติด้วย AI (GPT-4) และส่งแจ้งเตือนผ่าน Telegram

## 🎯 คุณสมบัติ

- ✅ วิเคราะห์ Sentiment ของข่าวการเงินด้วย GPT-4
- ✅ ให้ผลการวิเคราะห์แบบ 3 ระดับ: **Bullish** (แนวโน้มขาขึ้น), **Bearish** (แนวโน้มขาลง), **Neutral** (เป็นกลาง)
- ✅ ส่งการแจ้งเตือนอัตโนมัติผ่าน Telegram Bot
- ✅ RESTful API สำหรับรับข้อมูลข่าว
- ✅ รองรับภาษาไทย
- ✅ พร้อม Deploy บน Cloud Platform (Heroku, Railway, etc.)

## 🛠️ เทคโนโลยีที่ใช้

- **Python 3.7+**
- **Flask** - Web Framework
- **OpenAI GPT-4** - AI สำหรับวิเคราะห์ Sentiment
- **Telegram Bot API** - ส่งการแจ้งเตือน

## 📋 Requirements

```
flask
openai
requests
python-dotenv
```

## 🚀 การติดตั้ง

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/news-alert-gpt.git
cd news-alert-gpt
```

### 2. ติดตั้ง Dependencies

```bash
pip install -r requirements.txt
```

### 3. ตั้งค่า Environment Variables

สร้างไฟล์ `.env` ในโฟลเดอร์โปรเจค:

```env
OPENAI_API_KEY=your_openai_api_key_here
TELEGRAM_BOT_TOKEN=your_telegram_bot_token_here
TELEGRAM_CHAT_ID=your_telegram_chat_id_here
```

#### วิธีหา API Keys:

**OpenAI API Key:**
1. ไปที่ https://platform.openai.com/api-keys
2. สร้าง API Key ใหม่
3. คัดลอก Key มาใส่ใน `.env`

**Telegram Bot Token:**
1. พูดคุยกับ [@BotFather](https://t.me/BotFather) บน Telegram
2. ใช้คำสั่ง `/newbot` เพื่อสร้าง Bot ใหม่
3. คัดลอก Token ที่ได้มาใส่ใน `.env`

**Telegram Chat ID:**
1. พูดคุยกับ [@userinfobot](https://t.me/userinfobot) บน Telegram
2. Bot จะแสดง Chat ID ของคุณ
3. คัดลอก ID มาใส่ใน `.env`

### 4. รันโปรแกรม

```bash
python main.py
```

Server จะรันที่ `http://0.0.0.0:8080`

## 📡 API Documentation

### POST `/analyze`

วิเคราะห์ความเชื่อมั่น (Sentiment) ของข้อความข่าว

#### Request

```http
POST /analyze
Content-Type: application/json

{
  "text": "ข้อความข่าวที่ต้องการวิเคราะห์"
}
```

#### Response (Success)

```json
{
  "result": "Bullish"
}
```

Status Code: `200 OK`

#### Response (Error)

```json
{
  "error": "Missing 'text' field"
}
```

Status Code: `400 Bad Request`

#### ผลการวิเคราะห์ที่เป็นไปได้

- `Bullish` - แนวโน้มเชิงบวก (ราคาน่าจะขึ้น)
- `Bearish` - แนวโน้มเชิงลบ (ราคาน่าจะลง)
- `Neutral` - เป็นกลาง (ไม่มีผลกระทบชัดเจน)

## 💡 ตัวอย่างการใช้งาน

### ใช้ cURL

```bash
curl -X POST http://localhost:8080/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "บริษัท XYZ ประกาศกำไรเพิ่มขึ้น 50% จากปีที่แล้ว"}'
```

### ใช้ Python

```python
import requests

url = "http://localhost:8080/analyze"
data = {
    "text": "ธนาคารกลางประกาศขึ้นดอกเบี้ย 0.25%"
}

response = requests.post(url, json=data)
print(response.json())
```

### ใช้ JavaScript (Node.js)

```javascript
const axios = require('axios');

const data = {
  text: "ราคาทองคำปรับตัวขึ้นแรงจากความกังวลเศรษฐกิจ"
};

axios.post('http://localhost:8080/analyze', data)
  .then(response => console.log(response.data))
  .catch(error => console.error(error));
```

## 📱 Telegram Notification

เมื่อมีการวิเคราะห์ข่าว ระบบจะส่งข้อความ 2 ข้อความไปยัง Telegram:

```
🧠 ข้อความ: บริษัท XYZ ประกาศกำไรเพิ่มขึ้น 50% จากปีที่แล้ว

📊 วิเคราะห์: Bullish
```

## 🌐 Deploy บน Cloud Platform

### Deploy บน Heroku

1. ติดตั้ง [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

2. Login และสร้าง App

```bash
heroku login
heroku create your-app-name
```

3. ตั้งค่า Environment Variables

```bash
heroku config:set OPENAI_API_KEY=your_key
heroku config:set TELEGRAM_BOT_TOKEN=your_token
heroku config:set TELEGRAM_CHAT_ID=your_chat_id
```

4. Deploy

```bash
git push heroku main
```

### Deploy บน Railway

1. ไปที่ [Railway.app](https://railway.app)
2. เชื่อมต่อ GitHub Repository
3. ตั้งค่า Environment Variables ในหน้า Settings
4. Deploy จะทำงานอัตโนมัติ

## 🔒 ความปลอดภัย

- ⚠️ **อย่า commit ไฟล์ `.env`** ลงใน Git (ไฟล์นี้ควรอยู่ใน `.gitignore`)
- ⚠️ **อย่าแชร์ API Keys** ในที่สาธารณะ
- ⚠️ **ตั้งค่า Rate Limiting** ถ้าใช้งาน Production เพื่อป้องกันการใช้ API เกินควร

## 📊 Use Cases

- 📈 **นักลงทุนหุ้น** - ติดตามข่าวตลาดหุ้นแบบ Real-time
- 💰 **นักเทรด Forex** - วิเคราะห์ข่าวเศรษฐกิจที่มีผลต่ออัตราแลกเปลี่ยน
- 🪙 **นักลงทุน Crypto** - ติดตามข่าวสำคัญที่ส่งผลต่อตลาด Crypto
- 🤖 **Trading Bot** - ใช้เป็นส่วนหนึ่งของระบบ Automated Trading
- 📰 **News Aggregator** - รวบรวมและวิเคราะห์ข่าวจากหลายแหล่ง

## 🧪 Testing

ทดสอบการทำงานของ API:

```bash
# ทดสอบข่าวเชิงบวก
curl -X POST http://localhost:8080/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "บริษัทประกาศจ่ายเงินปันผลสูงสุดเป็นประวัติการณ์"}'

# ทดสอบข่าวเชิงลบ
curl -X POST http://localhost:8080/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "บริษัทประกาศขาดทุนต่อเนื่องเป็นไตรมาสที่ 3"}'

# ทดสอบข่าวเป็นกลาง
curl -X POST http://localhost:8080/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "บริษัทเปิดสำนักงานสาขาใหม่ที่กรุงเทพฯ"}'
```

## 🛣️ Roadmap

- [ ] รองรับหลายภาษา (English, Chinese, Japanese)
- [ ] เพิ่ม Database สำหรับเก็บประวัติการวิเคราะห์
- [ ] Dashboard สำหรับดูสถิติ
- [ ] รองรับ Webhook สำหรับ Auto-fetch ข่าว
- [ ] เพิ่ม Sentiment Score (0-100)
- [ ] รองรับการวิเคราะห์หลายข่าวพร้อมกัน (Batch Analysis)

## 🤝 Contributing

Pull requests are welcome! สำหรับการเปลี่ยนแปลงใหญ่ กรุณาเปิด issue เพื่อหารือก่อน

## 📝 License

MIT License - สามารถนำไปใช้งานได้อย่างอิสระ

## 👨‍💻 Author

Your Name

## 📧 Contact

- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

---

**Made with ❤️ and AI**
