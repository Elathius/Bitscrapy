# Ruby side
require 'json'
require 'telegram_bot'

token = 'ADDTELEGRAMBOTTOKENHERE'
bot = TelegramBot.new(token: token)

bot.get_updates(fail_silently: true) do |message|
  puts "@#{message.from.username}: #{message.text}"
  command = message.get_command_for(bot)


  message.reply do |reply|
    case command
    when /start/i
      reply.text = "Im still under development! buh i can still /greet or /hello you! :D"
    when /greet/i
      reply.text = "Hello, #{message.from.first_name}. 🤖"
    when /hello/i
      reply.text = "Hello, #{message.from.first_name}. 🤖"
    when /status/i
      output_bit = JSON.parse(`python bitscrape.py`)
      output_rem = JSON.parse(`python remscrape.py`)
      reply.text = "Heres a quick summary: \n #{output_bit} AED @ Bitoasis \n  #{output_rem} INR @ Remitano"
    else
      reply.text = "I have no idea what #{command.inspect} means."
    end
    puts "sending #{reply.text.inspect} to @#{message.from.username}"
    reply.send_with(bot)
  end
end
