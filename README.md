# csce606-TwitterDeck
A Twitter Deck clone for digital humanitarian purpose 

## Installation
1. conda create -y -n crisisdeck python=3.8
2. conda activate crisisdeck
3. pip install -r requirements.txt
4. python server.py
4. python main.py

### Reminder of PyQt
Building new UI/resources after editing 
```
pyside6-rcc .\resources.qrc -o ./resources_rc.qrc
python update-ui.py 
```
Building new gRPC files after editing
```
cd protobufs/
python -m grpc_tools.protoc -I proto --python_out=. --grpc_python_out=. .\proto\CrisisDeck.proto
```


