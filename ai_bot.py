# This Python file uses the following encoding: utf-8
import telebot
import openai 
from envs import openaikey, telekey

openai.api_key = openaikey 
bot = telebot.TeleBot(telekey)

@bot.message_handler(commands=['start'])
def message_handler_start_main(message):
	msg = bot.send_message(message.chat.id, 'hey hi')
	return

prompt = "придумай локанчиный и короткий комплимент в одно предложение напиши только его."

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0301",
    messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": prompt},
        ]
)

result = ''
for choice in response.choices:
    result += choice.message.content
bot.send_message(707939820, result)

# bot.polling()
