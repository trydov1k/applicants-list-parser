import json

def get_settings():
    with open("settings.json") as json_file:
        settings = json.load(json_file)
        return settings

def chenge_settings(settings):
    with open('settings.json', 'w') as json_file:
        json.dump(settings, json_file)

def main():
    settings = get_settings()
    print("Какую настройку вы хотите изменить? (Введите её номер)\n")
    settings_names = list(settings.keys())
    for n in range(len(settings_names)):
        print(f'{n+1}) {settings_names[n]}')
    try:
        ans = int(input())
        change_setting_name = settings_names[ans-1]
        change_setting_value = input(f'Введите новое значение настройки {change_setting_name}\n')
        agree = int(input(f'Вы подтверждаете изменение значения настройки {change_setting_name} на значение {change_setting_value}? (1/0)\n'))
        if agree:
            settings[change_setting_name] = change_setting_value
            chenge_settings(settings)
        else:
            main()
    except:
        print('Error')
        main()

if __name__ == "__main__":
    main()