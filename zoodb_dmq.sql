--Select Animals page
SELECT * FROM Animals;

--Search By on Animals page
SELECT * FROM Animals WHERE (`Animal ID` = :searchby)
SELECT * FROM Animals WHERE Name LIKE %:searchby% ;
SELECT * FROM Animals WHERE Species LIKE %:searchby% ;
SELECT * FROM Animals WHERE Habitat LIKE %:searchby% ;
SELECT * FROM Keepers WHERE Name LIKE %:searchby% ;
SELECT * FROM Animals WHERE Injury LIKE %:searchby% ;
SELECT * FROM Animals WHERE (`Feeding ID`= :searchby) ;

--might change to search by Keeper Name instead of KeeperID on website
--Update Animals column values

UPDATE Animals SET Animal ID =:newAnimalID,Name=:newName,Species=:newSpecies,Habitat=:newHabitat,Injury=:newInjury,Feeding ID=:newFeedingID 
WHERE = Animal ID =:oldAnimalID,Name=:oldName,Species=:oldSpecies,Habitat=:oldHabitat,Injury=:oldInjury,Feeding ID=:oldFeedingID;

--Remove Animal column values
DELETE FROM Animals 
WHERE Animal ID = :AnimalID,Name= :Name,Species=:Species,Habitat=:Habitat,Injury=:Injury,Feeding ID=:FeedingID 

--Note: need to add join statement and look into the select statements for values

--Add a new Animal

--Add values to Animal
INSERT INTO Animals(Animal ID,Name,Species,Age,Habitat,Keeper,Feeding Time,Injury)
VALUES (:Animal ID, :Name, :Species, :Age, :Habitat, :Feeding Time, :Injury,
(SELECT Keeper ID FROM Keepers WHERE Name = :Name)); 

--Add values to Schedule
INSERT INTO Feeding Times(Animal ID,Feeding Time ID,Diet,Time)
VALUES((SELECT Animal ID FROM Animals WHERE Animal ID =:Animal ID),:Feeding Time, :Diet, :Time); 

--Add values to Diet 
INSERT INTO Diet(Diet,Foods)
VALUES(:Diet,:Foods);

--Feeding Schedule Page
UPDATE Feeding Times SET Feeding Time ID =:newFeedingID,Diet=:newDiet,Time=:newTime
WHERE Feeding Time ID =:oldFeedingTimeID, Diet=:oldDiet, Time=:oldTime; 

--Diets Page 
UPDATE Diet SET Diet=:newDiet,Foods=:newFoods
WHERE Diet =:oldDiet, Foods=:oldFoods; 

--Care Instruction Page 

--Update Care Instructions
UPDATE Special Care Instructions SET Injury=:newInjury,Bandaging=:newBandaging,Medicine=:newMedicine
WHERE Injury =:oldInjury, Bandaging=:oldBandaging,Medicine=:oldMedicine; 

--Remove Care Instructions
DELETE FROM Special Care Instructions 
WHERE Injury =:Injury, Bandaging=:Bandaging, Medicine=:Medicine;


--Keepers Page
--Update Keepers

UPDATE Keepers SET Keeper ID =:newKeeperID,Name=:newName,Job Title=:newJobTitle
WHERE Keeper ID=:oldKeeperID, Name=:oldName,Job Title=:oldJobTitle;

--Remove Keepers
DELETE FROM Keepers 
WHERE Keeper ID =:Keeper ID,Name=:Name,Job Title=:JobTitle;

--Add Keeper 
INSERT INTO Keepers(Keeper ID,Name,Job Title)
VALUES (:Keeper ID, :Name, :Job Title);






