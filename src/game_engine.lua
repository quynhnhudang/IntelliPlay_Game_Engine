-- Define NPC class with attributes and behavior methods
NPC = {}

function NPC:new(name, health, x, y)
    local newObj = {name = name, health = health, position = {x = x, y = y}}
    self.__index = self
    return setmetatable(newObj, self)
end

-- NPC moves based on provided x and y increments
function NPC:move(dx, dy)
    self.position.x = self.position.x + dx
    self.position.y = self.position.y + dy
    print(self.name .. " moved to position:", self.position.x, self.position.y)
end

-- NPC takes damage and updates health
function NPC:takeDamage(damage)
    self.health = self.health - damage
    print(self.name .. " took damage. Health is now:", self.health)
end

-- Initialize and start the game with an NPC
function initializeGame()
    print("Initializing Game...")
    local npc = NPC:new("Goblin", 100, 0, 0)
    npc:move(1, 2)
    npc:takeDamage(10)
end

initializeGame()
