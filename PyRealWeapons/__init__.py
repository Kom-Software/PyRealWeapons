from varibales import *
import random

def GetRandomWeapon():
    return random.choice(WeaponName)
def GetWeaponVaribalesByName(Weapon, Varibale):
    if Weapon in WeaponIndexes.keys:
        WeaponIndex = WeaponIndexes.values[Weapon]
        return (WeaponShotType[WeaponIndex], WeaponCountry[WeaponIndex], WeaponYear[WeaponIndex],
                WeaponBulletsType[WeaponIndex], WeaponOneMagazine[WeaponIndex], WeaponLenght[WeaponIndex],
                WeaponBarrelLenght[WeaponIndex])