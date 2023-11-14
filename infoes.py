import random
import discord

def infos():
    giving_info = ["Did you know that for centuries, people have harnessed the energy of river currents, using dams to control water flow. Hydropower is the world's biggest source of renewable energy by far, with China, Brazil, Canada, the U.S., and Russia being the leading hydropower producers. While hydropower is theoretically a clean energy source replenished by rain and snow, it also has several drawbacks. (Source from https://education.nationalgeographic.org/resource/renewable-energy-explained/ and image by Marcus Ganahl, https://unsplash.com/photos/white-water-falls-on-gray-concrete-bridge-kPsBGvnVwnU)",
               "Did you know that dams aren't the only way to use water for power: Tidal and wave energy projects around the world aim to capture the ocean's natural rhythms. Marine energy projects currently generate an estimated 500 megawatts of power—less than one percent of all renewables—but the potential is far greater. Programs like Scotland’s Saltire Prize have encouraged innovation in this area. (Source from https://education.nationalgeographic.org/resource/renewable-energy-explained/ and image by Lucian B, https://unsplash.com/photos/green-trees-beside-brown-wooden-fence-GENc1ZnN8JI)",
               "Did you know that harnessing the wind as a source of energy started more than 7,000 years ago. Now, electricity-generating wind turbines are proliferating around the globe, and China, the U.S., and Germany are the world's leading wind-energy producers. From 2001 to 2017, cumulative wind capacity around the world increased to more than 539,000 megawatts from 23,900 megawatts—more than 22 fold. (Source from https://education.nationalgeographic.org/resource/renewable-energy-explained/ and image by Shawn Bagley, https://unsplash.com/photos/white-wind-turbines-during-daytime-CFbgCynTkEA)",
               "Did you know that another problem with wind turbines is that they’re a danger for birds and bats, killing hundreds of thousands annually, not as many as from glass collisions and other threats like habitat loss and invasive species, but enough that engineers are working on solutions to make them safer for flying wildlife. (Source from https://education.nationalgeographic.org/resource/renewable-energy-explained/ and image by Vincent van Zalinge, https://unsplash.com/photos/selective-focus-photography-of-blue-kingfisher-vUNQaTtZeOo)",
               "Did you know that in addition to solar panels, which convert the sun's light to electricity, concentrating solar power (CSP) plants use mirrors to concentrate the sun's heat, deriving thermal energy instead. China, Japan, and the U.S. are leading the solar transformation, but solar still has a long way to go, accounting for around just two percent of the total electricity generated in the U.S. in 2017. Solar thermal energy is also being used worldwide for hot water, heating, and cooling. (Source from https://education.nationalgeographic.org/resource/renewable-energy-explained/ and image by Andres Siimon, https://unsplash.com/photos/black-solar-panels-on-purple-flower-field-during-daytime-fCv4k5aAZf4)",
               "Did you know that biomass energy includes biofuels, such as ethanol and biodiesel, wood, wood waste, biogas from landfills, and municipal solid waste. Like solar power, biomass is a flexible energy source, able to fuel vehicles, heat buildings, and produce electricity. But biomass can raise thorny issues. (Source from https://education.nationalgeographic.org/resource/renewable-energy-explained/ and image by Soliman Cifuentes, https://unsplash.com/photos/a-close-up-of-a-tree-with-a-blue-sky-in-the-background-aM40YTAwM4s)",
               "Did you know that used for thousands of years in some countries for cooking and heating, geothermal energy is derived from Earth’s internal heat. On a large scale, underground reservoirs of steam and hot water can be tapped through wells that can go a two kilometers deep or more to generate electricity. On a smaller scale, some buildings have geothermal heat pumps that use temperature differences several meters below ground for heating and cooling. Unlike solar and wind energy, geothermal energy is always available, but it has side effects that need to be managed, such as the rotten-egg smell that can accompany released hydrogen sulfide. (Source from https://education.nationalgeographic.org/resource/renewable-energy-explained/ and image by Matt Palmer, https://unsplash.com/photos/smoke-coming-out-of-the-land-UXjYy04EvOc)"]

    randominfo = random.choice(giving_info)
    if randominfo == giving_info[0]:
        with open('images/Hydropower.jpg', 'rb') as f:
            # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
            picture = discord.File(f)
    # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
        return randominfo, picture
    
    if randominfo == giving_info[0]:
        with open('images/Hydropower.jpg', 'rb') as f:
            # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
            picture = discord.File(f)
    # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
        return randominfo, picture
    
    if randominfo == giving_info[1]:
        with open('images/dams.jpg', 'rb') as f:
            # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
            picture = discord.File(f)
    # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
        return randominfo, picture
    
    if randominfo == giving_info[2]:
        with open('images/Wind Turbines.jpg', 'rb') as f:
            # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
            picture = discord.File(f)
    # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
        return randominfo, picture
    
    if randominfo == giving_info[3]:
        with open('images/Birds.jpg', 'rb') as f:
            # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
            picture = discord.File(f)
    # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
        return randominfo, picture
    
    if randominfo == giving_info[4]:
        with open('images/Solar Panels.jpg', 'rb') as f:
            # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
            picture = discord.File(f)
    # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
        return randominfo, picture
    
    if randominfo == giving_info[5]:
        with open('images/Woods.jpg', 'rb') as f:
            # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
            picture = discord.File(f)
    # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
        return randominfo, picture
    
    if randominfo == giving_info[6]:
        with open('images/Geothermal.jpg', 'rb') as f:
            # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
            picture = discord.File(f)
    # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
        return randominfo, picture

def intro():
    introduction = "Hello! I'm a bot about climate change and how we can use renewable energy sources to prevent it! Here are some of my commands:\n!takeinfo : Learn a fact about renewable energy sources and benefits of it!\n!giveinfo X : Type your information instead of X and the bot will reply with it's thoughts on it!"
    with open('images/Renewable sources.jpg', 'rb') as f:
            # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
            picture = discord.File(f)
    # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    return introduction, picture