# Create Rocketry app
from rocketry import Rocketry
from api.model.optionsEnum_model import ChooseSnmpVersion
from api.service.snmp_checks_service import check_all_devices
app = Rocketry(config={"task_execution": "async"})


# Create some tasks

@app.task('minutely')
async def check_all_devices_scheduler():
    snmp = ChooseSnmpVersion
    await check_all_devices(snmp.v3)

if __name__ == "__main__":
    app.run()