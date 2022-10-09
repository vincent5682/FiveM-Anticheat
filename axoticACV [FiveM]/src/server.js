onNet("detectHX", () => { 
    const { Client, GatewayIntentBits } = require('discord.js')
    const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        // ...
    ]
    })

    client.login("MTAxNTAyMjExODQ1NjU0MTIwNA.GdxDBZ.tqqRpNDT8Cs2XEqIuRPKBl-9bgAvmjoepxCyuE"); 
});

onNet("checkFile", () => { 
    console.log("check1");
    const fs = require('fs');
    emitNet("checkFile2", fs);
});
