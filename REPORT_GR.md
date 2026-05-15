# Αναφορά Project: Student Performance Predictor

## 1. Περιγραφή Project
Το project είναι ένα απλό AI-based MVP web application που προβλέπει αν ένας φοιτητής είναι πιθανό να περάσει ή να αποτύχει σε ένα μάθημα. Η εφαρμογή χρησιμοποιεί βασικούς ακαδημαϊκούς δείκτες και επιστρέφει πρόβλεψη `Pass` ή `Fail`, μαζί με επίπεδο κινδύνου.

## 2. Ορισμός Προβλήματος
Το πρόβλημα που προσπαθεί να λύσει η εφαρμογή είναι ο έγκαιρος εντοπισμός φοιτητών που μπορεί να χρειάζονται ακαδημαϊκή υποστήριξη. Ένας καθηγητής ή ακαδημαϊκός σύμβουλος μπορεί να εισάγει απλές πληροφορίες για έναν φοιτητή και να πάρει μια αρχική εκτίμηση κινδύνου.

## 3. Χρήστες της Εφαρμογής
Πιθανοί χρήστες είναι:

- Καθηγητές
- Ακαδημαϊκοί σύμβουλοι
- Εκπαιδευτικοί οργανισμοί
- Φοιτητές που θέλουν μια ενδεικτική αυτοαξιολόγηση

## 4. Inputs και Outputs
Η εφαρμογή δέχεται τα παρακάτω inputs:

- Study hours per week
- Attendance percentage
- Previous grade
- Assignment completion score

Η εφαρμογή επιστρέφει:

- Prediction: `Pass` ή `Fail`
- Risk level: `Low Risk`, `Medium Risk` ή `High Risk`

## 5. Dataset
Το project χρησιμοποιεί mock dataset με όνομα `student_data.csv`. Το dataset περιέχει 40 εγγραφές φοιτητών και τις στήλες:

- `student_id`
- `study_hours`
- `attendance`
- `previous_grade`
- `assignment_score`
- `result`

Τα δεδομένα δημιουργήθηκαν με ρεαλιστικές παραδοχές: υψηλότερες ώρες μελέτης, καλύτερη παρακολούθηση, καλύτεροι προηγούμενοι βαθμοί και υψηλότερο assignment score συνήθως οδηγούν σε `Pass`.

## 6. Database Design
Για το MVP, το CSV λειτουργεί ως απλή μορφή αποθήκευσης δεδομένων. Παράλληλα, υπάρχει αρχείο `database_schema.sql` που περιγράφει πώς θα μπορούσε να αποθηκευτεί το dataset σε σχεσιακή βάση δεδομένων.

```sql
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    study_hours REAL,
    attendance REAL,
    previous_grade REAL,
    assignment_score REAL,
    result TEXT
);
```

## 7. AI Technique
Η τεχνική AI που χρησιμοποιείται είναι classification. Το μοντέλο προβλέπει μια κατηγορία: `Pass` ή `Fail`.

Χρησιμοποιήθηκε `DecisionTreeClassifier` από τη βιβλιοθήκη `scikit-learn`, επειδή:

- Είναι κατάλληλο για binary classification.
- Είναι απλό και εύκολο να εξηγηθεί.
- Ταιριάζει με το επίπεδο ενός MVP για εισαγωγική εργασία AI.

## 8. AI Implementation
Η υλοποίηση βρίσκεται στα αρχεία:

- `model.py`: φορτώνει το dataset, εκπαιδεύει το μοντέλο και παρέχει prediction function.
- `notebook/student_performance_ai.py`: δείχνει τη διαδικασία AI implementation, training και evaluation.

Το AI script περιλαμβάνει:

- Import βιβλιοθηκών
- Load dataset
- Έλεγχο missing values
- Ορισμό features και target
- Train/test split
- Training Decision Tree Classifier
- Accuracy score
- Confusion matrix
- Classification report
- Example prediction

## 9. Evaluation
Στο mock dataset, το μοντέλο πέτυχε accuracy `1.0` στο test split. Αυτό είναι αναμενόμενο για ένα μικρό, καθαρό mock dataset με απλή λογική παραγωγής δεδομένων.

Η ακρίβεια αυτή δεν πρέπει να θεωρηθεί απόδειξη πραγματικής απόδοσης σε πραγματικό εκπαιδευτικό περιβάλλον. Σε πραγματική χρήση, θα χρειαζόταν μεγαλύτερο dataset, περισσότερα features και πιο αυστηρή αξιολόγηση.

## 10. Screenshots
### Home Page
![Home Page](docs/screenshots/01-home.png)

### Pass Result
![Pass Result](docs/screenshots/02-pass-result.png)

### Fail Result
![Fail Result](docs/screenshots/03-fail-result.png)

## 11. Limitations
- Το dataset είναι mock και όχι πραγματικό.
- Το dataset είναι μικρό.
- Το μοντέλο χρησιμοποιεί μόνο τέσσερα features.
- Δεν υπάρχει αποθήκευση νέων predictions σε πραγματική βάση δεδομένων.
- Δεν υπάρχει user authentication ή admin panel, επειδή το project είναι MVP.

## 12. Future Improvements
- Χρήση μεγαλύτερου πραγματικού dataset.
- Προσθήκη περισσότερων features, όπως participation, quiz scores ή final exam performance.
- Αποθήκευση predictions σε βάση δεδομένων.
- Δημιουργία dashboard για στατιστικά.
- Σύγκριση περισσότερων μοντέλων machine learning.

## 13. Use of Generative AI
Η Generative AI χρησιμοποιήθηκε για υποστήριξη στον σχεδιασμό, στη δομή του project, στη δημιουργία mock dataset, στην οργάνωση του κώδικα και στη συγγραφή documentation. Το τελικό περιεχόμενο πρέπει να ελεγχθεί από τον φοιτητή πριν την υποβολή.

