#!/usr/bin/env python3

import random
import time, datetime
from PIL import ImageColor

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
    brands['jewelry'] = ['Invicta Reserve Jewelry', 'Gems en Vogue', 'Dallas Prince Designs', 'Pamela McCoy Jewelry', 'Michael Valitutti', 'Sonia Bitton', 'Joya', 'Victoria Wieck', 'Signare', 'Chuck Clemency', 'Effy Jewelry', 'Paul Deasy Designs', 'Gem Treasures', 'Kristen Amato', 'Tagliamonte', 'NYC II Jewelry', 'Hanover Jewelry', 'One World Jewelry', 'Park Avenue Collection', 'Passage to Israel']
    brands['watches'] = ['Invicta', 'Bulova', 'Seiko', 'Citizen', 'Movado', 'Glycine', 'Aragon', 'Bulova Accutron', 'Swiss Legend', 'Android', 'Stuhrling Original', 'Croton', 'Akribos XXIV', 'Tissot', 'Raymond Weil', 'Renato', 'Swiss Military', 'Edox', 'Versace Watches', 'Mondaine']
    brands['fashion'] = ['One World', 'Kate & Mallory', 'Jill Martin', 'WDNY', 'Pamela McCoy Fashions', 'Onyx Nite', 'Guiliana Rancic Collection', 'Indigo Thread Co.', 'Donna Salyers Fabulous Furs', 'Marc Bouwer', 'Christopher & Banks (exclusive lines)', 'Maya Collection', 'Karl Lagerfeld Paris', 'MarlaWynne', 'Fit 4 U', 'Couture Collection by Antthony', 'Sharif Handbags & Fashion', 'Brooks Brothers (licensed apparel)', 'Love, Carson by Carson Kressley', 'OSO Casuals']
    brands['beauty']  = ['Skinn Cosmetics', 'Elizabeth Grant', 'Isomers Skincare', 'Consult Beaute by Heather & Terry Dubrow', 'Beekman 1802', 'Ready to Wear', 'Michael Todd Beauty', 'Manuela Marcheggiani Skincare', 'PRAI Beauty', 'Serious Skincare', 'Pure Cosmetics', 'Trilogy Skincare', 'Foreo', 'Suzanne Somers Organics', 'Dermelect', 'Grande Cosmetics', 'Peter Thomas Roth', 'L’Occitane', 'BeautyBio', 'StriVectin']
    brands['health']  = ['Vitauthority', 'Dr. Dubrow Health & Wellness', 'Beekman 1802 (supplements & wellness)', 'Consult Health by Heather & Terry Dubrow', 'True2Life Supplements', 'PurCore Nutrition', 'Isomers Wellness', 'PRAI Ageless Nutrition', 'PureHealth Research', 'Herbal Harvest', 'VitaTree Nutritionals', 'Probiotic America', 'Joyce Giraud Renewal Supplements', 'Andrew Lessman Procaps', 'Nature’s Code', 'Invigorate Health', 'Swisa Beauty Wellness', 'Balance of Nature', 'Healthy Directions', 'Life Extension']
    brands['home']    = ['Margaritaville Home', 'DeLonghi', 'Dyson', 'Ninja Kitchen', 'Cuisinart', 'KitchenAid', 'Vitamix', 'Cook’s Companion', 'Waterford Crystal', 'Royal Doulton', 'Lenox', 'Temp-tations', 'Bell & Howell', 'SodaStream', 'Sharper Image', 'Corkcicle', 'Mikasa', 'Tagliaferri Home Collection', 'Donatella Home', 'Blueair']
    brands['food']    = ['Margaritaville Foods', 'Junior’s Cheesecake', 'Gourmet Holiday', 'Rochester Meat Company', 'Authentic Gourmet Croissants', 'David’s Cookies', 'Rastelli’s Fine Foods', 'Kansas City Steaks', 'Heartland Fresh', 'Mackenzie Limited', 'In-Law’s Foods', 'Farmer Jon’s Popcorn', 'Custom Bakehouse', 'Main Street Gourmet', 'Famous Amos', 'Omaha Steaks (select items)', 'Mrs. Prindable’s Caramel Apples', 'Broadway Basketeers', 'Ghirardelli', 'Harry London Chocolates']
    return brands

def GetMaterials():
    materials = {}
    materials['jewelry'] = ['24K gold', '18K gold', '14K gold', '10K gold', 'sterling silver', 'platinum', 'palladium', 'rose gold', 'white gold', 'yellow gold', 'cubic zirconia', 'diamond', 'sapphire', 'emeralds', 'rubie', 'amethyst', 'topaz', 'opal', 'garnet', 'tanzanite']
    materials['watches'] = ['stainless steel', 'titanium', 'ceramic', 'sapphire crystal', 'mineral crystal', 'carbon fiber', 'resin', 'leather', 'rubber straps', 'silicone straps', 'nylon bands', 'gold plating', 'rose gold plating', 'ion plating', 'mother-of-pearl dials', 'diamond accents', 'luminous paint', 'bronze cases', 'polyurethane', 'canvas straps']
    materials['fashion'] = ['cotton', 'linen', 'silk', 'wool', 'cashmere', 'polyester', 'rayon', 'nylon', 'spandex', 'modal', 'viscose', 'denim', 'chiffon', 'velvet', 'faux fur', 'faux leather', 'sequin fabric', 'lace', 'jersey knit', 'tweed']
    materials['beauty']  = ['hyaluronic acid', 'retinol', 'vitamin C', 'collagen', 'peptides', 'shea butter', 'jojoba oil', 'argan oil', 'aloe vera', 'niacinamide', 'glycolic acid', 'salicylic acid', 'coconut oil', 'rosehip oil', 'tea tree oil', 'ceramides', 'green tea extract', 'charcoal', 'manuka honey', 'squalane']
    materials['health']  = ['multivitamins', 'omega-3 fish oil', 'collagen peptides', 'glucosamine', 'chondroitin', 'MSM', 'turmeric', 'ginger root', 'echinacea', 'probiotics', 'prebiotics', 'vitamin D3', 'calcium citrate', 'magnesium oxide', 'coenzyme Q10', 'resveratrol', 'ashwagandha', 'melatonin', 'zinc', 'iron']
    materials['home']    = ['stainless steel', 'tempered glass', 'hardwood', 'bamboo', 'ceramic', 'porcelain', 'nonstick coating', 'cast iron', 'enamel', 'polycarbonate', 'polypropylene', 'microfiber', 'memory foam', 'down feathers', 'stoneware', 'crystal', 'cotton', 'wool blend', 'aluminum', 'silicone']
    materials['food']    = ['chocolate', 'vanilla', 'caramel', 'strawberries', 'blueberries', 'almonds', 'pecans', 'walnuts', 'cheddar cheese', 'cream cheese', 'butter', 'sugar', 'maple syrup', 'beef', 'chicken breast', 'pork ribs', 'salmon', 'shrimp', 'croissant dough', 'sourdough bread']

    return materials

def GetAspects():
    aspects = {}
    aspects['jewelry'] = ['precious metal', 'gemstone', 'carat weight', 'cut and clarity', 'birthstone', 'plated finish', 'handcrafted', 'designer exclusive', 'statement pieces', 'collectible value', 'tennis bracelets', 'vintage inspired', 'modern minimalism', 'engraved detail', 'luxury appeal', 'affordable glamour', 'holiday gifting', 'lifetime warranty']
    aspects['watches'] = ['automatic movement', 'quartz movement', 'Swiss made', 'water resistance', 'chronograph features', 'skeleton dials', 'limited editions', 'oversized cases', 'stainless steel bands', 'leather straps', 'interchangeable bands', '24-hour subdials', 'luminous hands', 'tourbillon styling', 'date windows', 'tachymeter bezel', 'collector exclusives', 'luxury packaging', 'sport inspired', 'everyday wear']
    aspects['fashion'] = ['seasonal collections', 'stretch fabrics', 'exclusive prints', 'layering pieces', 'figure flattering', 'boho chic', 'office ready', 'casual weekend', 'evening wear', 'red carpet inspired', 'faux fur accents', 'vegan leather', 'easy care fabrics', 'mix and match sets', 'limited runs', 'designer collaborations', 'comfort focus', 'trend driven', 'versatile basics', 'holiday sparkle']
    aspects['beauty']  = ['anti-aging', 'hydration focus', 'clinical formulas', 'natural ingredients', 'paraben free', 'dermatologist tested', 'celebrity endorsed', 'spa inspired', 'targeted serums', 'bold pigments', 'long wear makeup', 'all-in-one kits', 'home devices', 'luxury packaging', 'travel size options', 'exclusive bundles', 'fragrance collections', 'cruelty free', 'made in USA', 'global beauty trends']
    aspects['health']  = ['immune support', 'joint health', 'collagen boosting', 'daily vitamins', 'antioxidants', 'digestive health', 'protein powders', 'sleep aids', 'energy boosters', 'omega-3 supplements', 'bone strength', 'metabolism support', 'mood balance', 'heart health', 'detox cleanses', 'probiotic formulas', 'celebrity doctor developed', 'capsules and powders', 'subscription refills', 'wellness kits']
    aspects['home']    = ['kitchen appliances', 'cookware sets', 'crystal accents', 'holiday décor', 'air purifiers', 'robot vacuums', 'bedding sets', 'memory foam', 'multi-use gadgets', 'organization solutions', 'space saving design', 'energy efficiency', 'luxury finishes', 'hostess gifts', 'indoor lighting', 'outdoor living', 'pet friendly', 'easy cleanup', 'modern design', 'classic styling']
    aspects['food']    = ['gourmet desserts', 'holiday tins', 'ready to bake', 'flash frozen', 'restaurant quality', 'small batch', 'family recipes', 'hand decorated', 'snack assortments', 'gift baskets', 'individually wrapped', 'comfort food classics', 'artisan crafted', 'regional specialties', 'imported chocolates', 'steakhouse cuts', 'breakfast favorites', 'seasonal flavors', 'easy heat and serve', 'subscription boxes']

    return aspects

def GetTypes():
    types = {}
    types['jewelry'] = ['ring', 'necklace', 'bracelet', 'earrings', 'pendant', 'brooch', 'anklet', 'cuff bracelet', 'charm bracelet', 'hoop earrings', 'stud earrings', 'drop earrings', 'tennis bracelet', 'cocktail ring', 'wedding band', 'engagement ring', 'locket', 'beaded necklace', 'choker', 'jewelry set']
    types['watches'] = ['diver watch', 'chronograph watch', 'dress watch', 'sports watch', 'pilot watch', 'field watch', 'digital watch', 'automatic watch', 'quartz watch', 'skeleton watch', 'GMT watch', 'luxury watch', 'limited edition watch', 'smartwatch', 'pocket watch', 'minimalist watch', 'tactical watch', 'fashion watch', 'oversized watch', 'daily wear watch']
    types['fashion'] = ['dress', 'blouse', 'tunic', 't-shirt', 'sweater', 'cardigan', 'jacket', 'coat', 'leggings', 'jeans', 'skirt', 'shorts', 'romper', 'jumpsuit', 'shawl', 'poncho', 'maxi dress', 'cocktail dress', 'evening gown', 'two-piece set']
    types['beauty']  = ['lipstick', 'lip gloss', 'foundation', 'concealer', 'powder', 'eyeshadow palette', 'eyeliner', 'mascara', 'blush', 'bronzer', 'highlighter', 'primer', 'setting spray', 'serum', 'face cream', 'eye cream', 'cleanser', 'toner', 'facial mask', 'fragrance']
    types['health']  = ['multivitamin bottle', 'collagen powder tub', 'protein shake mix', 'capsule supplement', 'gummy vitamins', 'sleep aid tablets', 'joint health formula', 'immune booster powder', 'probiotic capsules', 'omega-3 softgels', 'bone health tablets', 'energy booster shots', 'green drink mix', 'detox tea', 'digestive enzyme capsules', 'vitamin D drops', 'herbal tincture', 'powdered electrolyte mix', 'wellness kit', 'subscription refill pack']
    types['home']    = ['stand mixer', 'blender', 'toaster oven', 'air fryer', 'coffee maker', 'slow cooker', 'cookware set', 'knife set', 'glassware set', 'bakeware set', 'vacuum cleaner', 'robot vacuum', 'air purifier', 'humidifier', 'bedding set', 'comforter', 'area rug', 'lamp', 'wall clock', 'storage container set']
    types['food']    = ['cheesecake', 'steak', 'chicken breast pack', 'pork rib rack', 'shrimp platter', 'lobster tails', 'salmon fillet', 'croissant', 'bagel', 'sourdough loaf', 'cookie tin', 'brownie tray', 'cupcake assortment', 'candy box', 'caramel apple', 'popcorn tin', 'holiday ham', 'pasta kit', 'breakfast bundle', 'gourmet gift basket']
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
    cat = item['category']
    
    banner = random.choice(['30-Day Money Back Guarantee', '30-Day Money Back Guarantee', '30-Day Money Back Guarantee', '60-Day Money Back Guarantee', '90-Day Money Back Guarantee', 'BMSM%', 'BMSM$', 'PWP%', 'PWP$'])
    if banner == 'BMSM%':
        banner = 'Buy One, Get One for ' + str(random.choice([10, 15, 15, 20])) + '% OFF'
    elif banner == 'BMSM$':
        banner = 'Buy One, Get One for $' + str(random.choice([3, 5, 5, 10])) + ' OFF'
    elif banner == 'PWP%' or banner == 'PWP$':
        number = GetItemNumber()
        types = GetTypes()
        item   = random.choice(types[cat]).title()
        if banner == 'PWP%':
            banner = 'Add ' + number + ' - ' + item + ' - Receive ' + str(random.choice([10, 15, 15, 20])) + '% OFF'
        if banner == 'PWP$':
            banner = 'Add ' + number + ' - ' + item + ' - Save $' + str(random.choice([3, 5, 5, 10]))
            
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
        coupon['url']   = f"ShopHQ.com/{coupon['code']}"
    elif coupon['kind'] != None:
        coupon['line2'] = f"{item['category'].upper()} ORDERS"
        coupon['code']  = f"{item['category'].upper()}{coupon['discount']}"
        coupon['url']   = f"ShopHQ.com/{item['category']}"

    return coupon

#price formatting
def PriceRange(price):
    if len(price) == 1:
        return f"${price[0]:,.2f}"
    elif len(price) == 2:
        return f"${price[0]:,.2f}" + '/' + f"${price[-1]:,.2f}"
    elif len(price) > 2:
        return f"${price[0]:,.2f}" + '-' + f"${price[-1]:,.2f}"
    else:
        return '$'

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
    item['y']           = 0
    item['image']       = ''

    return item

#main tower maker
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

    item['x']           = x = random.randint(123, int(1920*.75))
    print(item)
    return item

MakeItem()
