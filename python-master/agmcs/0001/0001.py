import uuid

uuids = []
for i in range(2):
	uuids.append(uuid.uuid1())
print(uuids)
