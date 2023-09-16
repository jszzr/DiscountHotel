# Architecture Overview
- emulator.py: 
    - Simulates temperature fluctuations based on a specified schedule. 
        - Defines three modes, each altering the temperature at varying rates and incurring different charges
        - When the emulator starts, increase temperature. Automatically stop when reach target temperature, and decrease temperature
    - Count the running time of the emulator
    - Compute the total fees of based on schedule and running time

- scheduler.py:
    - Manages two queues: one for running emulators and another for waiting emulators
        - Stores the ID of each emulator instance, prioritizing the emulators with higher priority
    - Considers the maximum number of running emulators as resources. When these resources are available, they are allocated to the waiting emulators
    - Has the ability to start new emulators and stop currently running ones

- client.py
    - sends four types of commands to server: start, stop, change target temperature, change wind speed
        - first establish connection with server
        - print command results according to server response like "start an emulator successfully"
    - create a GUI to choose commands and present responded information from server like total fees
    - define a temperature which can be used to initate emulator

- server.py
    - 