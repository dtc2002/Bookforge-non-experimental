#!/bin/bash

# Load environment variables from JSON
export APP_URL="https://bookforge.example.com"
export DATABASE_URL="postgres://user:password@localhost/bookforge_db"
export JWT_SECRET="supersecretkey123"
export EMAIL_SERVICE="smtp://user:password@smtp.example.com"
export STRIPE_API_KEY="sk_test_1234567890"
export AWS_ACCESS_KEY_ID="AKID1234567890ABCDEF"
export AWS_SECRET_ACCESS_KEY="wJalrXUtnFEB7u2jnk7f53479B16b2g6YXu87T1R"

# Verify variables are set
if [ -z "$(env | grep -E 'APP_URL|DATABASE_URL|JWT_SECRET|EMAIL_SERVICE|STRIPE_API_KEY|AWS_ACCESS_KEY_ID|AWS_SECRET_ACCESS_KEY')" ]; then
  echo "Error: Required environment variables not set"
  exit 1
fi