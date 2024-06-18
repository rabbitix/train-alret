import logging
import time
import warnings
from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from utils import send_message_to_user, raja_trains, check_mr_bilit

logging.basicConfig(level=logging.INFO)
warnings.filterwarnings("ignore")


class AlertProcess:

    def start(self):
        logging.info("Starting Alert Process")
        self._start()

    def _start(self):
        scheduler = BlockingScheduler()
        scheduler.add_job(
            self._check_trains,
            trigger='interval',
            next_run_time=datetime.now(),
            minutes=20,
        )
        scheduler.start()

    def _check_raja(self) -> bool:
        params_list = [
            "UbtQervSWWZU00Vkn jX8606nvyglQZ5SCP8tTfsNSWA3yIlT9J3mctAWyQ3oFLHDW5SopnLgyDNYeh7f2UWZTuISbE/G4LL vAfZicHJJo=",
            "t4Mia71Tg/immgoEwE8SpLmkD566APS3UQVp3l2u6iVIMUAYoDYxWcx 6LbHVkG/JgFqcZvINVhh7o9FqNS6pLZh8yIo3Rn9BE/g10GqCHA=",
            "0kdbzWEl2Ao8WJ/cPg3JMEFzcbFFQ90LaObW6qwaa3zXEce4UZYCjjXaLa24YbzKuRnZsBdeVGhVPJW2h3OfIcPA8e3v5BreJJFCxKw4ReM="
        ]
        raja_results = []
        for query in params_list:
            result = raja_trains(query)
            raja_results.append(result)
        return any(raja_results)

    def _check_mr_bilit(self):
        dates = [
            "2024-06-22",
            "2024-06-23",
            "2024-06-24",
            "2024-06-25",
            "2024-06-26",
        ]
        mr_results = []
        for date in dates:
            res = check_mr_bilit(date)
            time.sleep(0.5)
            mr_results.append(res)
        return any(mr_results)

    def _check_trains(self):
        admin_list = [194419690,
                      632655173
                      ]
        check_1 = False  # self._check_raja()
        check_2 = self._check_mr_bilit()

        if check_2 or check_1:
            for user in admin_list:
                logging.info(f"send msg to {user}")
                send_message_to_user(user)


if __name__ == '__main__':
    instance = AlertProcess()
    instance.start()
