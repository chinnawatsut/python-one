import sys
import os

super_country = {'TH': 'ไทย',
                 'GE': 'เยอรมัน',
                 'JP': 'ญี่ปุ่น',
                 'US': 'สหรัฐ'}

print(super_country['TH'])

del super_country['JP']

super_country['JP'] = 'ญี่ปุ่น'

print(len(super_country))

print(super_country.get('JP'))

print(super_country.keys())

print(super_country.values())