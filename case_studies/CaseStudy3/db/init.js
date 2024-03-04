// Connect to the 'CaseStudy3' database or create it if it doesn't exist
var cstd_db = db.getSiblingDB('CaseStudy3');

// Create a collection named "users" within the 'CaseStudy3' database
db.createCollection("users");