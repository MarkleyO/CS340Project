# CS340Project
## Sample Data ##

### animals ###
| Animal ID | Name  | Species    | Age | Habitat  | Keeper ID | Feeding Time ID | Injury         |
|-----------|-------|------------|-----|----------|-----------|-----------------|----------------|
| 001E      | Elsa  | Polar Bear | 10  | Tundra   | 001       | 001             | Cut            |
| 002J      | Julian| Lemur      | 3   | Jungle   | 002       | 002             | Common Cold    |
| 003S      | Shira | Kangaroo   | 6   | Outback  | 003       | 003             | Sprained Ankle |

### feedingTimes ###
| Feeding Time ID | Animal ID | Diet    | Time |
|-----------------|-----------|---------|------|
| 001             | 001E      | Fish    | 5    |
| 002             | 002J      | Fruit   | 4    |
| 003             | 003S      | Grasses | 13   |

### diets ###
| Diet    | Food                       |
|---------|----------------------------|
| Fish    | Tuna, Salmon, Trout        |
| Fruit   | Tamarind, Tamarillo, Seeds |
| Grasses | Wheat Grass, Flowers, Fern |

### specialCareInstructions ###
| Injury         | Bandaging  | Medicine     |
|----------------|------------|--------------|
| Cut            | Gauze      | NULL         |
| Common Cold    | NULL       | Antibiotics  |
| Sprained Ankle | Ankle Wrap | Pain Killers |

### keepers ###
| Keeper ID | Name  | Job Title            |
|-----------|-------|----------------------|
| 001       | Mina  | Head Keeper          |
| 002       | Steve | Herbivore Specialist |
| 003       | Naomi | Keeper               |

## Relations ##
- care to animals (1:M)
- animals to keepers (M:M)
- animals to feeding times (1:1)
- feeding times to diets (1:1)
