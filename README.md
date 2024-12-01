# django_referral


This is a simple django app with the imitation of a referral system.

- Users can authorize via phone number;
- System imitates SMS with 4-digit code:
- System generates for a user unique 6-symbol referral code
- Each user can use only one referral code
- The user profile API provides a list of other users (phones) that entered a referral code

## API

GET /api/referrals/{user_id} - gets a list of users (phones) that used the referral code from the {user_id} in json format.

For example: GET /api/referrals/1 gets response: [{"user":1,"phone":"+12125552368"}]

