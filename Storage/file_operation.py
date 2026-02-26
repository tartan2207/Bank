import datetime
from Utils.exception import BankError, FileNotFound, NotFilePermission
import json
class FileOperation:

    @staticmethod
    def create_json( *args)->dict :
        acount_id, type, transaction_id, amount, result_message= args
        transaction_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {
            "id_acount": acount_id,
            "id_transaction":transaction_id,
            "date": transaction_time,
            "type":type,
            "amount" : amount,
            "result": result_message
        }
        return data
    @staticmethod
    def save_log(path_file, *args):
        data=FileOperation.create_json(*args)
        try:
            with open(path_file, 'a', encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except PermissionError as ex:
            raise NotFilePermission("Помилка: Відсутні права доступу до файла") from ex
        except FileNotFoundError as ex:
            raise FileNotFound("Файл не знайдено ") from ex
        except IOError as ex:
            print(f"IO помилка: {ex}")
        except BankError as e:
            print(f"Непередбачена помилка: {e}")
        print()

    @staticmethod
    def read_log(path_file):
        try:
            with open(path_file, 'r',encoding="utf-8") as file:
                data = json.load(file)
                string_json=json.dumps(data, indent=4, ensure_ascii = False)
        except PermissionError as ex:
            raise NotFilePermission("Помилка: Відсутні права доступу до файла") from ex
        except FileNotFoundError as ex:
            raise FileNotFound("Файл не знайдено ") from ex
        except json.JSONDecodeError as e:
            print(f"Помилка при декодуванні JSON. {e}")
        except BankError as e:
            print(f"Непередбачена помилка: {e}")
        else:
            print(string_json)

