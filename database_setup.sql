CREATE TABLE pnms (
    "id" serial PRIMARY KEY,
    "first_name" text NOT NULL,
    "last_name" text NOT NULL,
    "email" text NOT NULL,
    "student_id" text NOT NULL,
    "phone" text NOT NULL,
    "year" text NOT NULL,
    "school" text NOT NULL,
    "comments" text NOT NULL
);

CREATE TABLE event_attendance (
  "student_id" text primary key,
  "day" date
);