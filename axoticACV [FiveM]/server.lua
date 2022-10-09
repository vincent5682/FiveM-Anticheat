require "os"

local validPlayers = {}

AddEventHandler('playerConnecting', function(name, setCallback, deferrals)
    local source = source
    
    deferrals.defer()
    Wait(0)
    deferrals.update("Checking for verification...")

    if not isValidPlayer(source) then
        deferrals.done("Sorry, AxoticAC could not verify")
    else
        deferrals.done()
    end
end)

Citizen.CreateThread(function()
    while true do
        Citizen.Wait(3000)
        loadValidPlayers()
        checkPlayers()
    end
end)

function loadValidPlayers()
    local timestamp = os.time(os.date('*t')) - 30
    local date = os.date("%Y-%m-%d %H:%M:%S", timestamp)
    local result = MySQL.Sync.fetchAll("SELECT * FROM axoticac.user WHERE verify = 1 AND lastupdated > @date", {
        ['@date'] = date
    })

    validPlayers = result
end

function checkPlayers()
    for _, player in ipairs(GetPlayers()) do
        if not isValidPlayer(player) then
            DropPlayer(player, "Kicked by AxoticAC | Reason: could not verify") --kick player
        end
    end
end

function isValidPlayer(player)
    local steamid = getIdentifier(player, "steam")
    local ip = getIdentifier(player, "ip")

	for _, v in pairs(validPlayers) do
        if v.steamid == steamid and v.ip == ip then
            return true
        end
	end
	return false
end

function getIdentifier(player, property)
	for k,v in pairs(GetPlayerIdentifiers(player))do
        if string.sub(v, 1, string.len(property .. ":")) == property .. ":" then
            return v:gsub(property .. ":", "")
        end
	end
end
