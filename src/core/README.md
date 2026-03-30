core is where the main code that leads to game engines, are. Unities, combat, inputs, view engines and major engines are here.

manager_data: Get any json data when the GameLoop starts
manager_flow: Decide what mode is running in the game, being able to be Combat Mode or Exploration Mode. Default and actuals unique value is Combat.
manager_level: Is a LevelBuilder instance that makes the combat/exploration terrain and entities based on level_data.
manager_save: Controls the exportation, saving and loading player data.
manager_sprites: working on it yet, but the idea is organize the character sprites automatically rendering them without the need of change state values.