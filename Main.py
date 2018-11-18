def main():
    
    import schedule
    import time
    import DiscordBotManager

    schedule.every().day.at("03:00").do(DiscordBotManager.requestpraise)
    schedule.every().day.at("06:00").do(DiscordBotManager.requestpraise)
    schedule.every().day.at("09:00").do(DiscordBotManager.requestpraise)
    schedule.every().day.at("12:00").do(DiscordBotManager.requestpraise)
    schedule.every().day.at("15:00").do(DiscordBotManager.requestpraise)
    schedule.every().day.at("18:00").do(DiscordBotManager.requestpraise)
    schedule.every().day.at("21:00").do(DiscordBotManager.requestpraise)
    schedule.every().day.at("24:00").do(DiscordBotManager.requestpraise)
    DiscordBotManager.requestpraise()

    while True:
        schedule.run_pending()
        time.sleep(1) # wait one minute


main()