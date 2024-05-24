# -*- coding: utf-8 -*-

def decrease_quality(item):
    if not (item.quality <= 0):
        if item.sell_in < 0 or item.name == 'Conjured Mana Cake':
            item.quality = item.quality - 2
        else:
            item.quality = item.quality - 1

    return item.quality


def increase_quality(item):
    if not (item.quality >= 50):
        if item.name == 'Backstage passes to a TAFKAL80ETC concert':
            if 5 <= item.sell_in <= 10:
                item.quality = item.quality + 2
            elif item.sell_in <= 5:
                item.quality = item.quality + 3
        else:
            item.quality = item.quality + 1

    return item.quality


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.sell_in = item.sell_in - 1

            if item.name not in ['Aged Brie', 'Sulfuras, Hand of Ragnaros',
                                 'Backstage passes to a TAFKAL80ETC concert']:
                item.quality = decrease_quality(item)

            if item.name in ['Aged Brie', 'Backstage passes to a TAFKAL80ETC concert']:
                item.quality = increase_quality(item)

#backstage passed both increase and decrease

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
