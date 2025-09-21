#!/usr/bin/env python3

import random
import time, datetime
import sys
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor, ImageTk
import textwrap
import qrcode
import tkinter as tk
from screeninfo import get_monitors
import keyboard

#make it kind of random
rng = random.SystemRandom()
random.seed(rng.randint(1, 1000))

#color codes and min prices
def MakeCategorie(color, minPrice):
    categorie = {}
    categorie['color']    = ImageColor.getrgb(color)
    categorie['minPrice'] = minPrice
    return categorie

def GetCategories():
    categories = {}
    categories['jewelry'] = MakeCategorie('#008ad0', 500.0)
    categories['watches'] = MakeCategorie('#fdb90b', 200.0)
    categories['fashion'] = MakeCategorie('#6460ac', 20.0)
    categories['health']  = MakeCategorie('#f3711b', 30.0)
    categories['beauty']  = MakeCategorie('#daa9bf', 50.0)
    categories['home']    = MakeCategorie('#04b34a', 75.0)
    categories['food']    = MakeCategorie('#c91e49', 50.0)
    return categories

#sku / item number
def GetItemNumber():
    first = '{:03d}'.format(random.randint(1, 999))
    last  = '{:03d}'.format(random.randint(1, 999))
    return first + '-' + last

#topline info
def GetBrands():
    brands = {}
    brands['jewelry'] = [
        'Invicta Reserve Jewelry™', 'Gems en Vogue®', 'Dallas Prince Designs™', 'Pamela McCoy Jewelry™',
        'Michael Valitutti™', 'Sonia Bitton®', 'Joya™', 'Victoria Wieck®', 'Chuck Clemency™', 'Effy Jewelry®',
        'Paul Deasy Designs™', 'Gem Treasures®', 'Tagliamonte®', 'NYC II Jewelry™', 'Passage to Israel™',
        'Todd Waziak Designs™', 'Tanzanite Gems®', 'Matthew Favaloro™', 'Bellarosa™', 'Gem Insider®',
        'Park Avenue Collection™', 'Golden Odyssey™', 'Portofino®', 'Korite Ammolite®', 'Samuel B.®',
        'Vanna K®', 'Samantha DeStefano™', 'LaBell®', 'Gem Afficionado™', 'GemHaven™',
        'Sigal Style®', 'Stefano Oro®', 'Kristen Amato™', 'One World Jewelry™', 'Hanover Jewelry™',
        'Signare™', 'Zahra™', 'Passions by Dweck®', 'Michael Shellis™', 'Absolute Gems™'
    ]
    brands['watches'] = [
        'Invicta®', 'Bulova®', 'Seiko®', 'Citizen®', 'Movado®', 'Glycine®', 'Aragon®', 'Accutron®',
        'Swiss Legend®', 'Stuhrling Original®', 'Croton®', 'Akribos XXIV®', 'Tissot®',
        'Raymond Weil®', 'Renato®', 'Swiss Military™', 'Edox®', 'Versace Watches®',
        'Mondaine®', 'Android®', 'Adee Kaye™', 'Lucien Piccard®', 'Charriol®', 'Technomarine®',
        'Swiss Diamond®', 'Luminox®', 'Longines®', 'Wenger®', 'Tag Heuer®', 'Concord®',
        'August Steiner®', 'Bulova Precisionist™', 'Accutron II™', 'Swiss Invincible™',
        'Momo Design®', 'Gevril®', 'XOSkeleton®', 'Graham London®', 'Bovet®', 'Perrelet®'
    ]
    brands['fashion'] = [
        'One World®', 'Kate & Mallory®', 'Jill Martin™', 'WDNY®', 'Pamela McCoy Fashions™', 'Onyx Nite™',
        'Guiliana Rancic Collection™', 'Indigo Thread Co.™', 'Donna Salyers Fabulous Furs®', 'Marc Bouwer®',
        'Christopher & Banks®', 'Karl Lagerfeld Paris®', 'MarlaWynne®', 'Fit 4 U®', 'Couture Collection by Antthony®',
        'Sharif®', 'Brooks Brothers®', 'Love, Carson by Carson Kressley™', 'OSO Casuals™', 'Maya Collection™',
        'Glitterscape®', 'Kathy Ireland Fashions®', 'Christopher Fink™', 'Linea Donatella™', 'Elan®',
        'NYDJ®', 'French Dressing Jeans®', 'Sharif Handbags®', 'Colette Green™', 'Madi Claire®',
        'Anuschka®', 'Dooney & Bourke®', 'Coach®', 'Kate Spade®', 'Michael Kors®',
        'Gucci®', 'Louis Vuitton®', 'Fendi®', 'Prada®', 'Versace®'
    ]
    brands['beauty'] = [
        'Skinn Cosmetics®', 'Elizabeth Grant®', 'Isomers Skincare®', 'Consult Beaute™', 'Beekman 1802®',
        'Ready to Wear®', 'Michael Todd Beauty®', 'PRAI Beauty®', 'Serious Skincare®', 'Pure Cosmetics™',
        'Trilogy Skincare®', 'Foreo®', 'Suzanne Somers Organics™', 'Dermelect®', 'Grande Cosmetics®',
        'Peter Thomas Roth®', 'L’Occitane®', 'BeautyBio™', 'StriVectin®', 'Manuela Marcheggiani Skincare™',
        'Lancôme®', 'Clinique®', 'Estée Lauder®', 'IT Cosmetics™', 'Tarte™',
        'Urban Decay®', 'Bobbi Brown®', 'Smashbox®', 'NARS®', 'Laura Geller®',
        'Mally Beauty®', 'Josie Maran®', 'Philosophy®', 'Elemis®', 'Pür Minerals®',
        'Algenist®', 'Korres®', 'Origins®', 'Fresh®', 'Guerlain®'
    ]
    brands['health'] = [
        'Vitauthority®', 'Dr. Dubrow Health & Wellness™', 'Consult Health™', 'True2Life®', 'PurCore Nutrition™',
        'Isomers Wellness®', 'PRAI Ageless Nutrition™', 'PureHealth Research™', 'Herbal Harvest™', 'VitaTree Nutritionals®',
        'Probiotic America™', 'Joyce Giraud Renewal™', 'Andrew Lessman Procaps®', 'Nature’s Code®', 'Invigorate Health™',
        'Swisa Beauty Wellness™', 'Balance of Nature®', 'Healthy Directions®', 'Life Extension®', 'Vitacost®',
        'GNC®', 'Nature Made®', 'Centrum®', 'Alive!®', 'Garden of Life®',
        'NOW Foods®', 'Solgar®', 'Thorne®', 'Nature’s Bounty®', 'Optimum Nutrition®',
        'Herbalife®', 'Amway Nutrilite®', 'MegaFood®', 'New Chapter®', 'Vital Proteins®',
        'NeoCell®', 'Sports Research®', 'BioSchwartz®', 'Pure Encapsulations®', 'Doctor’s Best®'
    ]
    brands['home'] = [
        'Margaritaville Home™', 'DeLonghi®', 'Dyson®', 'Ninja®', 'Cuisinart®', 'KitchenAid®', 'Vitamix®',
        'Cook’s Companion™', 'Waterford®', 'Royal Doulton®', 'Lenox®', 'Temp-tations®', 'Bell & Howell®',
        'SodaStream®', 'Sharper Image®', 'Corkcicle®', 'Mikasa®', 'Blueair®', 'Donatella Home™', 'Tagliaferri Home™',
        'Calphalon®', 'All-Clad®', 'Le Creuset®', 'Staub®', 'Nordic Ware®',
        'Anchor Hocking®', 'Corelle®', 'Pyrex®', 'Farberware®', 'Oster®',
        'Hamilton Beach®', 'Bissell®', 'Shark®', 'Hoover®', 'iRobot®',
        'Dyson Pure Cool™', 'Simple Human®', 'Yankee Candle®', 'Lladro®', 'Spode®'
    ]
    brands['food'] = [
        'Margaritaville Foods™', 'Junior’s Cheesecake®', 'Gourmet Holiday™', 'Rochester Meat Company™', 'Authentic Gourmet™',
        'David’s Cookies®', 'Rastelli’s®', 'Kansas City Steaks®', 'Heartland Fresh™', 'Mackenzie Limited®',
        'In-Law’s Foods™', 'Farmer Jon’s®', 'Custom Bakehouse™', 'Main Street Gourmet™', 'Famous Amos®',
        'Omaha Steaks®', 'Mrs. Prindable’s®', 'Broadway Basketeers®', 'Ghirardelli®', 'Harry London®',
        'Godiva®', 'Lindt®', 'Ferrero Rocher®', 'See’s Candies®', 'Hershey’s®',
        'Nestlé®', 'Toblerone®', 'Brach’s®', 'Russell Stover®', 'Whitman’s®',
        'Entenmann’s®', 'Pepperidge Farm®', 'Hostess®', 'Keurig® (coffee)', 'Starbucks® (at-home)',
        'Caribou Coffee®', 'Gevalia®', 'Maxwell House®', 'Folgers®', 'Green Mountain Coffee®'
    ]
    return brands


def GetMaterials():
    materials = {}
    materials['jewelry'] = [
        '24K gold', '18K gold', '14K gold', '10K gold', 'sterling silver', 'platinum', 'palladium',
        'rose gold', 'white gold', 'yellow gold', 'cubic zirconia', 'diamond',
        'sapphire', 'emeralds', 'rubie', 'amethyst', 'topaz', 'opal', 'garnet', 'tanzanite'
    ]
    materials['watches'] = [
        'stainless steel', 'titanium', 'ceramic', 'sapphire crystal', 'mineral crystal', 'carbon fiber',
        'resin', 'leather', 'rubber straps', 'silicone straps', 'nylon bands', 'gold plating',
        'rose gold plating', 'ion plating', 'mother-of-pearl dials', 'diamond accents',
        'luminous paint', 'bronze cases', 'polyurethane', 'canvas straps'
    ]
    materials['fashion'] = [
        'cotton', 'linen', 'silk', 'wool', 'cashmere', 'polyester', 'rayon', 'nylon',
        'spandex', 'modal', 'viscose', 'denim', 'chiffon', 'velvet', 'faux fur',
        'faux leather', 'sequin fabric', 'lace', 'jersey knit', 'tweed'
    ]
    materials['beauty'] = [
        'hyaluronic acid', 'retinol', 'vitamin C', 'collagen', 'peptides', 'shea butter', 'jojoba oil',
        'argan oil', 'aloe vera', 'niacinamide', 'glycolic acid', 'salicylic acid', 'coconut oil',
        'rosehip oil', 'tea tree oil', 'ceramides', 'green tea extract', 'charcoal', 'manuka honey', 'squalane'
    ]
    materials['health'] = [
        'multivitamins', 'omega-3 fish oil', 'collagen peptides', 'glucosamine', 'chondroitin', 'MSM',
        'turmeric', 'ginger root', 'echinacea', 'probiotics', 'prebiotics', 'vitamin D3', 'calcium citrate',
        'magnesium oxide', 'coenzyme Q10', 'resveratrol', 'ashwagandha', 'melatonin', 'zinc', 'iron'
    ]
    materials['home'] = [
        'stainless steel', 'tempered glass', 'hardwood', 'bamboo', 'ceramic', 'porcelain', 'nonstick coating',
        'cast iron', 'enamel', 'polycarbonate', 'polypropylene', 'microfiber', 'memory foam', 'down feathers',
        'stoneware', 'crystal', 'cotton', 'wool blend', 'aluminum', 'silicone'
    ]
    materials['food'] = [
        'chocolate', 'vanilla', 'caramel', 'strawberries', 'blueberries', 'almonds', 'pecans',
        'walnuts', 'cheddar cheese', 'cream cheese', 'butter', 'sugar', 'maple syrup', 'beef',
        'chicken breast', 'pork ribs', 'salmon', 'shrimp', 'croissant dough', 'sourdough bread'
    ]
    return materials

def GetAspects():
    aspects = {}
    aspects['jewelry'] = [
        'precious metal', 'gemstone', 'carat weight', 'cut and clarity', 'birthstone', 'plated finish',
        'handcrafted', 'designer exclusive', 'statement pieces', 'collectible value', 'tennis bracelets',
        'vintage inspired', 'modern minimalism', 'engraved detail', 'luxury appeal',
        'affordable glamour', 'holiday gifting', 'lifetime warranty'
    ]
    aspects['watches'] = [
        'automatic movement', 'quartz movement', 'Swiss made', 'water resistance', 'chronograph features',
        'skeleton dials', 'limited editions', 'oversized cases', 'stainless steel bands', 'leather straps',
        'interchangeable bands', '24-hour subdials', 'luminous hands', 'tourbillon styling', 'date windows',
        'tachymeter bezel', 'collector exclusives', 'luxury packaging', 'sport inspired', 'everyday wear'
    ]
    aspects['fashion'] = [
        'seasonal collections', 'stretch fabrics', 'exclusive prints', 'layering pieces', 'figure flattering',
        'boho chic', 'office ready', 'casual weekend', 'evening wear', 'red carpet inspired',
        'faux fur accents', 'vegan leather', 'easy care fabrics', 'mix and match sets',
        'limited runs', 'designer collaborations', 'comfort focus', 'trend driven', 'versatile basics', 'holiday sparkle'
    ]
    aspects['beauty'] = [
        'anti-aging', 'hydration focus', 'clinical formulas', 'natural ingredients', 'paraben free',
        'dermatologist tested', 'celebrity endorsed', 'spa inspired', 'targeted serums', 'bold pigments',
        'long wear makeup', 'all-in-one kits', 'home devices', 'luxury packaging', 'travel size options',
        'exclusive bundles', 'fragrance collections', 'cruelty free', 'made in USA', 'global beauty trends'
    ]
    aspects['health'] = [
        'immune support', 'joint health', 'collagen boosting', 'daily vitamins', 'antioxidants', 'digestive health',
        'protein powders', 'sleep aids', 'energy boosters', 'omega-3 supplements', 'bone strength',
        'metabolism support', 'mood balance', 'heart health', 'detox cleanses', 'probiotic formulas',
        'celebrity doctor developed', 'capsules and powders', 'subscription refills', 'wellness kits'
    ]
    aspects['home'] = [
        'kitchen appliances', 'cookware sets', 'crystal accents', 'holiday décor', 'air purifiers',
        'robot vacuums', 'bedding sets', 'memory foam', 'multi-use gadgets', 'organization solutions',
        'space saving design', 'energy efficiency', 'luxury finishes', 'hostess gifts', 'indoor lighting',
        'outdoor living', 'pet friendly', 'easy cleanup', 'modern design', 'classic styling'
    ]
    aspects['food'] = [
        'gourmet desserts', 'holiday tins', 'ready to bake', 'flash frozen', 'restaurant quality', 'small batch',
        'family recipes', 'hand decorated', 'snack assortments', 'gift baskets', 'individually wrapped',
        'comfort food classics', 'artisan crafted', 'regional specialties', 'imported chocolates',
        'steakhouse cuts', 'breakfast favorites', 'seasonal flavors', 'easy heat and serve', 'subscription boxes'
    ]
    return aspects

def GetTypes():
    types = {}
    types['jewelry'] = [
        'ring', 'necklace', 'bracelet', 'earrings', 'pendant', 'brooch', 'anklet', 'cuff bracelet',
        'charm bracelet', 'hoop earrings', 'stud earrings', 'drop earrings', 'tennis bracelet',
        'cocktail ring', 'wedding band', 'engagement ring', 'locket', 'beaded necklace', 'choker', 'jewelry set'
    ]
    types['watches'] = [
        'diver watch', 'chronograph watch', 'dress watch', 'sports watch', 'pilot watch',
        'field watch', 'digital watch', 'automatic watch', 'quartz watch', 'skeleton watch',
        'GMT watch', 'luxury watch', 'limited edition watch', 'smartwatch', 'pocket watch',
        'minimalist watch', 'tactical watch', 'fashion watch', 'oversized watch', 'daily wear watch'
    ]
    types['fashion'] = [
        'dress', 'blouse', 'tunic', 't-shirt', 'sweater', 'cardigan', 'jacket', 'coat', 'leggings',
        'jeans', 'skirt', 'shorts', 'romper', 'jumpsuit', 'shawl', 'poncho', 'maxi dress',
        'cocktail dress', 'evening gown', 'two-piece set'
    ]
    types['beauty'] = [
        'lipstick', 'lip gloss', 'foundation', 'concealer', 'powder', 'eyeshadow palette',
        'eyeliner', 'mascara', 'blush', 'bronzer', 'highlighter', 'primer', 'setting spray',
        'serum', 'face cream', 'eye cream', 'cleanser', 'toner', 'facial mask', 'fragrance'
    ]
    types['health'] = [
        'multivitamin bottle', 'collagen powder tub', 'protein shake mix', 'capsule supplement', 'gummy vitamins',
        'sleep aid tablets', 'joint health formula', 'immune booster powder', 'probiotic capsules', 'omega-3 softgels',
        'bone health tablets', 'energy booster shots', 'green drink mix', 'detox tea', 'digestive enzyme capsules',
        'vitamin D drops', 'herbal tincture', 'powdered electrolyte mix', 'wellness kit', 'subscription refill pack'
    ]
    types['home'] = [
        'stand mixer', 'blender', 'toaster oven', 'air fryer', 'coffee maker', 'slow cooker', 'cookware set',
        'knife set', 'glassware set', 'bakeware set', 'vacuum cleaner', 'robot vacuum', 'air purifier', 'humidifier',
        'bedding set', 'comforter', 'area rug', 'lamp', 'wall clock', 'storage container set'
    ]
    types['food'] = [
        'cheesecake', 'steak', 'chicken breast pack', 'pork rib rack', 'shrimp platter', 'lobster tails',
        'salmon fillet', 'croissant', 'bagel', 'sourdough loaf', 'cookie tin', 'brownie tray', 'cupcake assortment',
        'candy box', 'caramel apple', 'popcorn tin', 'holiday ham', 'pasta kit', 'breakfast bundle', 'gourmet gift basket'
    ]
    return types

def GetTopline(item):
    category = item['category']
    brands    = GetBrands()
    materials = GetMaterials()
    aspects   = GetAspects()
    types     = GetTypes()

    if category in brands.keys():
        return random.choice(brands[category]) + ' ' + ( random.choice(materials[category]) + ' ' + random.choice(aspects[category]) + ' ' + random.choice(types[category]) ).title()
    else:
        return ''

#prices
def GetPrices(item):
    categories = item['categories']
    category   = item['category']
    markdown   = random.choice([False, False, True])
    pricerange = random.choice([1, 1, 1, 1, 2, 3])

    base = random.uniform(categories[category]['minPrice'], categories[category]['minPrice']*2)
    
    lists = []
    sales = []
    for x in range(pricerange):
        if len(sales) == 0:
            sales.append(base)
        else:
            sales.append(sales[-1]*1.25)
    
    if markdown:
        percent = random.choice([1.2, 1.3, 1.4, 1.5, 1.7, 1.9])
    else:
        percent = 1

    for x in sales:
        lists.append(x * percent)


    vp  = random.choice([1, 2, 3, 4, 5, 6])
    vps = []
    for x in sales:
        vps.append(x/vp)

    prices = {}
    prices['markdown'] = markdown
    prices['list']     = lists
    prices['sale']     = sales
    prices['vp']       = vp
    prices['vps']      = vps
    return prices

#price handle
def GetHandle(prices):
    if (prices['list'][0] > prices['sale'][0]) and (prices['list'][-1] > prices['sale'][-1]):
        return random.choice(['SALE PRICE', 'SALE PRICE', 'SALE PRICE', 'TODAY\'S TOP DEAL', 'ONCE ONLY', 'THIS DAY ONLY', 'THIS WEEK ONLY', 'MUST HAVE BUY', 'MUST HAVE BUY', 'SUPERCHARGED DEAL', 'WEEKLY DEAL'])
    else:
        return 'ShopHQ PRICE'

#tower color
def GetColor(item):
    handle     = item['handle']
    categories = item['categories']
    category   = item['category']
    
    colors = {}
    colors['red']  = '#e04035'
    colors['only'] = '#db0b5b'
    colors['must'] = '#b41b81'
    colors['deal'] = '#e7519d'
    colors['base'] = '#0e76bc'
    
    if 'TOP' in handle and 'DEAL' in handle:
        return colors['red']
    elif 'ONCE' in handle and 'ONLY' in handle:
        return colors['red']
    elif 'ONLY' in handle:
        return colors['only']
    elif 'MUST' in handle and 'HAVE' in handle:
        return colors['must']
    elif 'DEAL' in handle:
        return colors['deal']
    else:
        return colors['base']

#banner
def GetBanner(item):
    category   = item['category']
    
    banner = random.choice(['30-Day Money Back Guarantee', '30-Day Money Back Guarantee', '30-Day Money Back Guarantee', '60-Day Money Back Guarantee', '90-Day Money Back Guarantee', 'BMSM%', 'BMSM$', 'PWP%', 'PWP$'])
    if banner == 'BMSM%':
        banner = 'Buy One, Get One for ' + str(random.choice([10, 15, 15, 20])) + '% OFF'
    elif banner == 'BMSM$':
        banner = 'Buy One, Get One for $' + str(random.choice([3, 5, 5, 10])) + ' OFF'
    elif banner == 'PWP%' or banner == 'PWP$':
        number = GetItemNumber()
        types = GetTypes()
        item   = random.choice(types[category]).title()
        if banner == 'PWP%':
            banner = 'Add ' + item + ' - ' + number + ' - Receive ' + str(random.choice([10, 15, 15, 20])) + '% OFF'
        if banner == 'PWP$':
            banner = 'Add ' + item + ' - ' + number + ' - Save $' + str(random.choice([3, 5, 5, 10]))
    return banner

#coupon
def GetCoupon(item):
    coupon = {}
    coupon['kind'] = random.choice([None, None, 'ALL', item['category']])

    if coupon['kind'] != None:
        coupon['discount'] = random.randint(1, 6) * 10
        coupon['line1']    = f"{coupon['discount']}% OFF"

        days = random.randint(1, 5)
        end = (datetime.date.today() + datetime.timedelta(days=days)).strftime("%m/%d")
        coupon['time']     = f"Now - {end} at 11:59pm ET"
    
    if coupon['kind'] == 'ALL':
        coupon['line2'] = 'ALL ORDERS'
        coupon['code']  = f"SHOPHQ{coupon['discount']}"
        coupon['url']   = f"ShopHQ.com/v/{coupon['code']}"
    elif coupon['kind'] != None:
        coupon['line2'] = f"{item['category'].upper()} ORDERS"
        coupon['code']  = f"{item['category'].upper()}{coupon['discount']}"
        coupon['url']   = f"ShopHQ.com/c/{item['category']}"
    return coupon

#price formatting
def PriceRange(price):
    if len(price) == 1:
        return f"${price[0]:,.2f}"
    elif len(price) == 2:
        return f"${price[0]:,.2f}" + ' / ' + f"${price[-1]:,.2f}"
    elif len(price) > 2:
        return f"${price[0]:,.2f}" + ' - ' + f"${price[-1]:,.2f}"
    else:
        return '$'

#max width for multi line text
def WordWrap(text, width):
    output = ''
    for line in textwrap.wrap(text, width=width):
        if output != '':
            output += '\n' + line
        else:
            output = line
    return output

def Item():
    item = {}
    item['itemNumber']  = ''
    item['categories']  = ''
    item['category']    = ''
    item['description'] = ''
    item['markdown']    = ''
    item['listPrice']   = ''
    item['color']       = (0, 0, 0)
    item['handle']      = ''
    item['salePrice']   = ''
    item['payments']    = 0
    item['vpPrice']     = ''
    item['banner']      = ''
    item['coupon']      = ''
    item['x']           = 0
    item['y']           = 246
    item['image']       = ''
    return item

#main function to get item information
def MakeItem():
    item = Item()
    
    item['categories']  = GetCategories()
    item['category']    = random.choice(list(item['categories'].keys()))
    prices              = GetPrices(item)

    item['itemNumber']  = GetItemNumber()
    item['description'] = GetTopline(item)

    item['markdown']    = prices['markdown']
    item['listPrice']   = prices['list']
    item['handle']      = GetHandle(prices)
    item['color']       = GetColor(item)
    item['salePrice']   = prices['sale']
    item['payments']    = prices['vp']
    item['vpPrice']     = prices['vps']
    item['banner']      = GetBanner(item)
    item['coupon']      = GetCoupon(item)

    item['x']           = x = random.randint(246, int(3840*.75)) 
    return item

#file path used if script is comppiled with pyinstaller and fonts/images added to the exe
def GetPath(filename, sub):
    if getattr(sys, 'frozen', False):
        #exe
        base = sys._MEIPASS
        return os.path.join(base, filename)
    else:
        #normal script
        base = os.path.dirname(__file__)
        return os.path.join(base, sub, filename)

#image text
def TextSize(text, font):
    draw  = ImageDraw.Draw( Image.new("RGBA", (0, 0), (0,0,0,0)) )
    lines = text.split('\n')

    w = 0
    h = int(font.size * len(lines) * 1.20)

    for line in lines:
        lw  = int(draw.textlength(line, font=font))
        if lw > w:
            w = lw
    return w, h

#resize text to fit in a screen area
def MaxSize(text, font, color, width, height):
    draw  = ImageDraw.Draw( Image.new("RGBA", (0, 0), (0,0,0,0)) )
    
    w1, h1 = TextSize(text, font)

    image = Image.new("RGBA", (w1, h1), (0,0,0,0))
    draw  = ImageDraw.Draw(image)

    draw.text((0, 0), text, color, font=font)

    if w1 > width and h1 > height:
        image = image.resize((width, height))
    elif w1 > width:
        image = image.resize((width, h1))
    elif h1 > height:
        image = image.resize((w1,    height))
    return image

#image corners for rectangles
def MakeCorner(radius, fill):
    corner = Image.new('RGBA', (radius, radius), (0, 0, 0, 0))
    draw = ImageDraw.Draw(corner)
    draw.pieslice((0, 0, radius * 2, radius * 2), 180, 270, fill=fill)
    return corner

#image tower background rectangles
def MakeRectangle(size, radius, fill):
    width, height = size
    rectangle = Image.new('RGBA', size, fill)
    
    corner = MakeCorner(radius[0], fill)
    rectangle.paste(corner, (0, 0))
    
    corner = MakeCorner(radius[1], fill)
    rectangle.paste(corner.rotate(90), (0, height - radius[1]))

    corner = MakeCorner(radius[2], fill)
    rectangle.paste(corner.rotate(180), (width - radius[2], height - radius[2]))

    corner = MakeCorner(radius[3], fill)
    rectangle.paste(corner.rotate(270), (width - radius[3], 0))
    return rectangle

#image for tower topline/description
def MakeTopline(item):
    local = Image.new("RGBA", (680, 460), (0,0,0,0))
    draw = ImageDraw.Draw(local)

    item['y'] = 246

    #BG
    img = MakeRectangle((680, 460), radius=[15, 15, 15, 15], fill=(232, 231, 234))
    local.paste(img, (0, 0), img)

    #HR
    img = MakeRectangle((680, 2), radius=[0, 0, 0, 0], fill=(0, 0, 0))
    local.paste(img, (0, 84), img)

    #Item Number
    font = ImageFont.truetype(GetPath('MuseoSans-700.otf', '_fonts'), 86)
    w1, h1 = TextSize(item['itemNumber'], font)
    draw.text((20, -6), item['itemNumber'], (0, 0, 0), font=font)

    #Description
    font = ImageFont.truetype(GetPath('MuseoSans-500.otf', '_fonts'), 66)

    description = WordWrap(item['description'], width=18)
    text = MaxSize(description, font, (0, 0, 0), 640, 460-h1)
    local.paste(text, (20, h1), text)

    item['image'].paste(local, (item['x'], item['y']), local)

    item['y'] += 460
    return item

def MakeList(item):
    local = Image.new("RGBA", (680, 76), (0,0,0,0))
    draw = ImageDraw.Draw(local)

    item['y'] += 16
    
    if item['markdown']:
        #BG
        img = MakeRectangle((680, 76), radius=[15, 0, 0, 15], fill=(232, 231, 234))
        local.paste(img, (0, 0), img)

        font = ImageFont.truetype(GetPath('MuseoSans-500.otf', '_fonts'), 50)
        w1, h1 = TextSize('ShopHQ Price' + '  ', font)
        w2, h2 = TextSize(PriceRange(item['listPrice']),     font)

        #FG
        text = Image.new("RGBA", (w1+w2+10, h1), (0,0,0,0))
        dt   = ImageDraw.Draw(text)
        dt.text((0, 0),  'ShopHQ Price' + '  ', (0, 0, 0), font=font)
        dt.text((w1, 0), PriceRange(item['listPrice']),     (0, 0, 0), font=font)
        dt.rectangle((w1-10, (h2/2), w1+w2+10, (h2/2)+2), fill=(224, 64, 53))

        if w1+w2+5 > 640:
            text = text.resize((int(640), int(h1)))
        
        local.paste(text, (20, 10), text)

        item['image'].paste(local, (item['x'], item['y']), local)

        item['y'] += 76
    return item

def MakeSale(item):
    local = Image.new("RGBA", (680, 180), (0,0,0,0))
    draw = ImageDraw.Draw(local)

    #BG
    if item['markdown']:
        img = MakeRectangle((680, 180), radius=[0, 0, 0, 0],   fill=item['color'])
    else:
        img = MakeRectangle((680, 180), radius=[15, 0, 0, 15], fill=item['color'])
    local.paste(img, (0, 0), img)

    #FG
    font = ImageFont.truetype(GetPath('MuseoSans-700.otf', '_fonts'), 66)
    w1, h1 = TextSize(item['handle'], font)
    text = MaxSize(item['handle'], font, (255, 255, 255), 640, h1)
    local.paste(text, (20, 0), text)

    font = ImageFont.truetype(GetPath('MuseoSans-900.otf', '_fonts'), 100)
    w2, h2 = TextSize(item['handle'], font)
    text = MaxSize(PriceRange(item['salePrice']), font, (255, 255, 255), 640, h2)
    local.paste(text, (20, h1-10), text)

    item['image'].paste(local, (item['x'], item['y']), local)

    item['y'] += 180
    return item

def MakePayments(item):
    local = Image.new("RGBA", (680, 90), (0,0,0,0))
    draw = ImageDraw.Draw(local)
    
    if item['payments'] > 1:
        #BG
        img = MakeRectangle((680, 90), radius=[0, 0, 0, 0], fill=(232, 231, 234))
        local.paste(img, (0, 0), img)

        img = MakeRectangle((680, 2), radius=[0, 0, 0, 0],  fill=(100, 100, 100))
        local.paste(img, (0, 88), img)

        #FG
        font = ImageFont.truetype(GetPath('MuseoSans-500.otf', '_fonts'), 66)

        pay = str(item['payments']) + " ValuePay® " + PriceRange(item['vpPrice'])

        w1, h1 = TextSize(pay, font)
        text = MaxSize(pay, font, (0, 0, 0), 640, h1)
        local.paste(text, (20, 0), text)

        item['image'].paste(local, (item['x'], item['y']), local)

        item['y'] += 90
    return item

def MakeShipping(item):
    local = Image.new("RGBA", (680, 66), (0,0,0,0))
    draw = ImageDraw.Draw(local)

    #BG
    img = MakeRectangle((680, 66), radius=[0, 15, 15, 0], fill=(232, 231, 234))
    local.paste(img, (0, 0), img)

    #FG
    if item['salePrice'][0] >= 75.0 and item['salePrice'][-1] >= 75.0:
        font = ImageFont.truetype(GetPath('MuseoSans-900.otf', '_fonts'), 54)
        draw.text((20, 0), 'FREE SHIPPING', (224, 64, 53), font=font)
    else:
        font = ImageFont.truetype(GetPath('MuseoSans-900.otf', '_fonts'), 54)
        draw.text((20, 0), 'FREE S&H  ', (224, 64, 53), font=font)
        w1, h1 = TextSize('FREE S&H  ', font)
        
        font = ImageFont.truetype(GetPath('MuseoSans-500.otf', '_fonts'), 54)
        draw.text((20+w1, 0), "ORDERS $75+", (0, 0, 0), font=font)

    item['image'].paste(local, (item['x'], item['y']), local)

    item['y'] += 66
    return item

def MakeBanner(item):
    local = Image.new("RGBA", (680, 150), (0,0,0,0))
    draw = ImageDraw.Draw(local)

    item['y'] += 16

    #BG
    img = MakeRectangle((680, 150), radius=[15, 15, 15, 15], fill=item['color'])
    local.paste(img, (0, 0), img)

    #FG
    font = ImageFont.truetype(GetPath('MuseoSans-700.otf', '_fonts'), 60)

    if 'Guarantee' in item['banner']:
        w = 25
    elif 'Buy One' in item['banner']:
        w = 15
    else:
        w = 30
    banner = WordWrap(item['banner'], width=w)

    text = MaxSize(banner, font, (255, 255, 255), 640, 150)
    local.paste(text, (20, 0), text)

    item['image'].paste(local, (item['x'], item['y']), local)
    return item

def MakeContact(item):
    local = Image.new("RGBA", (680, 220), (0,0,0,0))
    draw = ImageDraw.Draw(local)

    #BG
    #Blue
    img = MakeRectangle((240, 220), radius=[15, 15, 0, 0], fill=(14, 118, 188))
    local.paste(img, (0, 0), img)
    #White
    img = MakeRectangle((440, 220), radius=[0, 0, 15, 15], fill=(232, 231, 234))
    local.paste(img, (240, 0), img)

    #Bug
    ratio = 0.81625
    width = 230
    img = Image.open(GetPath('ShopHQ.tif', '_images'), 'r')
    img = img.resize((int(width),int(width*ratio)))
    local.paste(img, (4, 16), img)

    #Website
    font = ImageFont.truetype(GetPath('MuseoSans-500.otf', '_fonts'), 66)
    draw.text((240+10, 20), "ShopHQ.com", (0, 0, 0), font=font)

    #Phone
    font = ImageFont.truetype(GetPath('MuseoSans-500.otf', '_fonts'), 58)
    draw.text((240+10, 120), "(800) 474-6762", (0, 0, 0), font=font)

    item['image'].paste(local, (item['x'], 1808), local)
    return item

def MakeCoupon(item):
    coupon = item['coupon']
    
    local = Image.new("RGBA", (800, 220), (0,0,0,0))
    draw = ImageDraw.Draw(local)

    #BG
    img = MakeRectangle((800, 220), radius=[15, 15, 15, 15], fill=(232, 231, 234))
    local.paste(img, (0, 0), img)

    #FG
    if coupon['kind'] != None:
        #qr
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=0,
        )
        qr.add_data(coupon['url'])
        qr.make(fit=True)
        qr = qr.make_image(fill_color=(0, 0, 0), back_color=(255, 255, 255, 0)).convert('RGBA')
        qr = qr.resize((194, 194))
        local.paste(qr, (14, 14), qr)

        #lines 1 & 2
        font = ImageFont.truetype(GetPath('MuseoSans-700.otf', '_fonts'), 60)
        w1, h1 = TextSize(coupon['line1'], font)
        text = MaxSize(coupon['line1'], font, (0, 0, 0), 800-230, h1)
        local.paste(text, (230, 0), text)
        w1, h1 = TextSize(coupon['line2'], font)
        text = MaxSize(coupon['line2'], font, (0, 0, 0), 800-230, h1)
        local.paste(text, (230, 50), text)

        #code
        font = ImageFont.truetype(GetPath('MuseoSans-500.otf', '_fonts'), 60)
        w1, h1 = TextSize(f"CODE: {coupon['code']}", font)
        text = MaxSize(f"CODE: {coupon['code']}", font, (224, 64, 53), 800-230, h1)
        local.paste(text, (230, 100), text)

        #time
        font = ImageFont.truetype(GetPath('MuseoSans-500.otf', '_fonts'), 40)
        w1, h1 = TextSize(coupon['time'], font)
        text = MaxSize(coupon['time'], font, (0, 0, 0), 800-230, h1)
        local.paste(text, (230, 160), text)

        x = 3840-246-800
        if item['x'] > 3840/2:
            x = 246
        y = random.choice([100, 1808])
        item['image'].paste(local, (x, y), local)
    return item

def MakeTower(item):
    item['image'] = Image.new("RGBA", (3840, 2160), (0,0,0,0))

    item = MakeTopline(item)
    item = MakeList(item)
    item = MakeSale(item)
    item = MakePayments(item)
    item = MakeShipping(item)
    item = MakeBanner(item)
    item = MakeContact(item)
    item = MakeCoupon(item)
    return item

def ExitOnKey():
    if keyboard.is_pressed('esc'):
        root.destroy()
        sys.exit(0)

def Disolve(images, label):
    alpha = 0
    while 1.0 > alpha:
        blended = ImageTk.PhotoImage(Image.blend(images[0], images[1], alpha))
        alpha   = alpha + 0.05
        time.sleep(0.05)
        label.config(image=blended)
        label.update()
        ExitOnKey()
        
    blended = ImageTk.PhotoImage(images[1])
    label.config(image=blended)
    label.update()
    return blended

def FormatImage(screen, image):
    screenwidth  = screen['width']
    screenheight = screen['height']

    imagewidth, imageheight = image.size

    if (imagewidth/imageheight) == (screenwidth/screenheight):
        width  = screenwidth
        height = screenheight
    elif (imagewidth/imageheight) > (screenwidth/screenheight):
        width  = screenwidth
        height = int( screenwidth  * (imageheight/imagewidth) )
    else:
        width  = int( screenheight / (imageheight/imagewidth) )
        height = screenheight
    
    x = int((screenwidth  - width)/2)
    y = int((screenheight - height)/2)

    local = Image.new("RGBA", (screenwidth, screenheight), (0,0,0,0))
    image = image.resize((width, height), Image.LANCZOS)
    local.paste(image, (x, y), image)
    return local

def GetWindows():
    windows      = []
    windowImages = []
    imageLabels  = []
    
    for monitor in get_monitors():
        win = tk.Toplevel(root)
        win.config(cursor="none")
        win.overrideredirect(True)
        win.geometry(f"{monitor.width}x{monitor.height}+{monitor.x}+{monitor.y}")
        windowImages.append( ImageTk.PhotoImage(Image.new("RGBA", (monitor.width, monitor.height), (0,0,0,0))) )
        imageLabels.append( tk.Label(win, image=windowImages[-1], bg='#3b3b3b') )
        imageLabels[-1].pack()
        windows.append({'window': win, 'image': windowImages[-1], 'label': imageLabels[-1], 'width': monitor.width, 'height': monitor.height, 'x': monitor.x, 'y': monitor.y})
    return windows

images    = list(range(2))
images[0] = Image.new("RGBA", (1920, 1080), (0,0,0,0))

root = tk.Tk()
root.config(cursor="none")
root.withdraw()

windows = GetWindows()

def Update():
    item = MakeItem()
    item = MakeTower(item)
    images[1] = item['image']

    for win in windows:
        tmp = images.copy()
        tmp[0] = FormatImage(win, tmp[0])
        tmp[1] = FormatImage(win, tmp[1])
        win['image'] = Disolve(tmp, win['label'])
        
    images[0] = images[1]
    for x in range(1000):
        time.sleep(.01)
        ExitOnKey()

    root.after(0, Update)

root.after(0, Update)
root.mainloop()
