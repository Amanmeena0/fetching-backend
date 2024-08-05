use crime;

-- select importation_of_girls_from_foreign_countries FROM crime_data;
ALTER TABLE crime_data
MODIFY COLUMN preparation_and_assembly_for_dacoity int; 
show columns from crime_data;