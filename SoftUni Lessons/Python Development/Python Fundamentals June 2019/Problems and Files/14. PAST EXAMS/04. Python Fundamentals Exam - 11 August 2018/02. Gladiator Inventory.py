inventory = [item for item in input().split(" ")]

while True:
    command = input()
    if command == "Fight!":
        break

    action = [item for item in command.split(" ")]

    if "Buy" in action:
        if action[1] not in inventory:
            inventory += [action[1]]

    elif "Trash" in action:
        trashed_item = action[1]
        if trashed_item in inventory:
            inventory.remove(trashed_item)

    elif "Repair" in action:
        repaired_item = action[1]
        if repaired_item in inventory:
            inventory.remove(repaired_item)
            inventory += [repaired_item]

    elif "Upgrade" in action:
        split_upgrade_command = [item for item in action[1].split("-")]
        if len(split_upgrade_command) > 1:
            upgraded_item = split_upgrade_command[0]
            upgrade_with = split_upgrade_command[1]
        else:
            continue
        if upgraded_item in inventory:
            upgrade = upgraded_item + ":" + upgrade_with
            inventory.insert(inventory.index(upgraded_item) + 1, upgrade)

print(" ".join(inventory))
