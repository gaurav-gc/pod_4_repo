laptops = [
    {
        "productName": "Apple Macbook Pro",
        "url": "https://www.apple.com/macbook-pro-13/",
        "types": [
            {
                "id": "1",
                "screen_size": "13-inch",
                "cpu": ["1.4GHz quad-core 8th-generation Intel Core i5 processor", "2.0GHz quad-core 10th-generation Intel Core i5 processor"],
                "ram": ["8GB", "16GB"],
                "storage": ["256GB SSD", "512 GB SSD"],
                "colors": ["space gray", "silver"],
                "price": [1299, 1499, 1799]
            },
            {
                "id": "2",
                "screen_size": "16-inch",
                "cpu": ["2.6GHz 6-core 9th-generation Intel Core i7 processor", "2.3GHz 8-core 9th-generation Intel Core i9 processor"],
                "ram": ["16GB"],
                "storage": ["512 GB SSD", "1 TB SSD"],
                "colors": ["space gray", "silver"],
                "price": [2399, 2799]
            }
        ],
        "description": "If you're after the latest and greatest laptop from Apple, we suggest you look into the 2020 model of the MacBook Pro. The headline Touch Bar – a thin OLED display at the top of the keyboard which can be used for any number of things, whether that be auto-suggesting words as you type or offering Touch ID so you can log in with just your fingerprint – is of course included. It's certainly retained Apple's sense of style, but it comes at a cost. This is a pricey machine, so you may want to consider one of the Windows alternatives. But, if you're a steadfast Apple diehard, this is definitely the best laptop for you!"
    },
    {
        "id": "2",
        "productName": "Dell XPS",
        "url": "https://www.dell.com/en-us/shop/dell-laptops/sr/laptops/xps-laptops?~ck=bt",
        "types": [
            {
                "id": "3",
                "screen_size": "13-inch",
                "cpu": ["11th Generation Intel Core i3-1115G4 Processor", "11th Generation Intel Core i5-1135G7 Processor"],
                "ram": ["8GB"],
                "storage": ["256GB SSD", "512 GB SSD", "1 TB SSD"],
                "colors": ['Platinum silver exterior', 'black interior'],
                "price": [999, 1099, 1149, 1249]
            },
            {
                "id": "4",
                "screen_size": "15-inch",
                "cpu": ["10th Generation Intel Core i5-10300H"],
                "ram": ["8GB", "16GB", "32GB", "64GB"],
                "storage": ["256 GB SSD", "512 GB SSD", "1 TB SSD", "2 TB SSD"],
                "colors": ["Frost White with White Palmrest", "Frost White with White Palmrest"],
                "price": [1199, 1299, 1399, 1749, 1999, 2299]
            }
        ],
        "description": "The Dell XPS is an absolutely brilliant laptop. The 2020  version rocks an 11th-generation Intel Core i3, i5 or i7 processor and a bezel-less ‘Infinity Edge’ display. This Dell XPS continues to be the most popular Windows laptop in the world. What’s more, there’s a wide range of customization options, so you can really make the Dell XPS the best laptop for your needs. "
    }
]

print(type(laptops))
# <class 'list'>


print(len(laptops))
# 2

print(type(laptops[0]))
# <class 'dict'>

print(len(laptops[1]["types"]))
# 2
print(laptops[1]["types"][0]["colors"][1])
