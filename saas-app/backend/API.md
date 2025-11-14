# API Endpoints

The Django REST API is exposed under the `/api/v1/` prefix and is protected with JWT authentication unless otherwise noted. Trailing slashes are required by the default router.

## Authentication

| Method | Path                     | Description                                     |
| ------ | ------------------------ | ----------------------------------------------- |
| POST   | `/api/v1/auth/register/` | Create a new user account.                      |
| POST   | `/api/v1/auth/login/`    | Obtain access and refresh JWT tokens.           |
| POST   | `/api/v1/auth/refresh/`  | Refresh the access token using a refresh token. |

## Accounts

| Method    | Path                     | Description                                                                                               |
| --------- | ------------------------ | --------------------------------------------------------------------------------------------------------- |
| GET       | `/api/v1/users/`         | List users (staff) or return the requesting user. Supports `?search=` and `?username=`/`?email=` filters. |
| POST      | `/api/v1/users/`         | Create a user (staff only).                                                                               |
| GET       | `/api/v1/users/{id}/`    | Retrieve a user.                                                                                          |
| PUT/PATCH | `/api/v1/users/{id}/`    | Update a user.                                                                                            |
| DELETE    | `/api/v1/users/{id}/`    | Delete a user.                                                                                            |
| GET       | `/api/v1/users/me/`      | Convenience endpoint for the authenticated user's profile.                                                |
| PATCH     | `/api/v1/users/profile/` | Update the authenticated user's profile details.                                                          |

## Dating

| Method               | Path                                      | Description                                                                                               |
| -------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| GET/POST             | `/api/v1/dating/profiles/`                | List or create dating profiles. Supports `?mine=true` to scope to the requester.                          |
| GET/PUT/PATCH/DELETE | `/api/v1/dating/profiles/{id}/`           | Manage a specific dating profile.                                                                         |
| POST                 | `/api/v1/dating/profiles/update_profile/` | Update the authenticated user's dating profile via service layer.                                         |
| GET/POST             | `/api/v1/dating/photos/`                  | List or upload profile photos for the authenticated user.                                                 |
| GET/PUT/PATCH/DELETE | `/api/v1/dating/photos/{id}/`             | Manage a specific profile photo.                                                                          |
| GET/PATCH            | `/api/v1/dating/preferences/{id}/`        | Retrieve or update match preferences for the authenticated user (ID is ignored and resolved server side). |
| GET/POST             | `/api/v1/dating/likes/`                   | List likes created by the user or like another user (`liked_id`).                                         |
| GET                  | `/api/v1/dating/matches/`                 | List matches that involve the authenticated user.                                                         |

## Astrology

| Method               | Path                                             | Description                                                                        |
| -------------------- | ------------------------------------------------ | ---------------------------------------------------------------------------------- |
| GET/POST             | `/api/v1/astrology/astrologers/`                 | List or register astrologers. Supports `?experience_years=` filter and `?search=`. |
| GET/PUT/PATCH/DELETE | `/api/v1/astrology/astrologers/{id}/`            | Manage a specific astrologer profile.                                              |
| GET/POST             | `/api/v1/astrology/kundli-profiles/`             | List or create kundli profiles. Non-staff only see their own.                      |
| GET/PUT/PATCH/DELETE | `/api/v1/astrology/kundli-profiles/{id}/`        | Manage a kundli profile.                                                           |
| GET                  | `/api/v1/astrology/kundli-matches/`              | List kundli match results (filterable with `?profile_id=`).                        |
| GET/POST             | `/api/v1/astrology/chat-sessions/`               | List or schedule chat sessions with astrologers. Filter with `?status=`.           |
| GET/PUT/PATCH/DELETE | `/api/v1/astrology/chat-sessions/{id}/`          | Manage a specific chat session.                                                    |
| POST                 | `/api/v1/astrology/chat-sessions/{id}/start/`    | Mark a chat session as started.                                                    |
| POST                 | `/api/v1/astrology/chat-sessions/{id}/complete/` | Complete a chat session with optional notes.                                       |

## Wedding Planner

| Method               | Path                                      | Description                                                               |
| -------------------- | ----------------------------------------- | ------------------------------------------------------------------------- |
| GET/POST             | `/api/v1/wedding/projects/`               | List or create wedding projects. Supports `?date=` filter and `?search=`. |
| GET/PUT/PATCH/DELETE | `/api/v1/wedding/projects/{id}/`          | Manage a wedding project.                                                 |
| GET/POST             | `/api/v1/wedding/guests/`                 | List or add guests (filter with `?project__id=` and `?rsvp_status=`).     |
| GET/PUT/PATCH/DELETE | `/api/v1/wedding/guests/{id}/`            | Manage a guest entry.                                                     |
| GET/POST             | `/api/v1/wedding/tasks/`                  | List or add tasks (filter with `?project__id=` and `?status=`).           |
| GET/PUT/PATCH/DELETE | `/api/v1/wedding/tasks/{id}/`             | Manage a task.                                                            |
| GET/POST             | `/api/v1/wedding/budget-items/`           | List or add budget line items (`?project__id=` filter).                   |
| GET/PUT/PATCH/DELETE | `/api/v1/wedding/budget-items/{id}/`      | Manage a budget item.                                                     |
| GET/POST             | `/api/v1/wedding/vendor-categories/`      | List or manage vendor categories.                                         |
| GET/PUT/PATCH/DELETE | `/api/v1/wedding/vendor-categories/{id}/` | Manage a vendor category.                                                 |
| GET/POST             | `/api/v1/wedding/vendors/`                | List or add vendors.                                                      |
| GET/PUT/PATCH/DELETE | `/api/v1/wedding/vendors/{id}/`           | Manage a vendor.                                                          |
| GET/POST             | `/api/v1/wedding/vendor-bookings/`        | List or create vendor bookings (`?project__id=`, `?status=` filters).     |
| GET/PUT/PATCH/DELETE | `/api/v1/wedding/vendor-bookings/{id}/`   | Manage a vendor booking.                                                  |

## Finance

| Method               | Path                                  | Description                                            |
| -------------------- | ------------------------------------- | ------------------------------------------------------ |
| GET/POST             | `/api/v1/finance/loans/`              | List or submit loan applications (`?status=` filter).  |
| GET/PUT/PATCH/DELETE | `/api/v1/finance/loans/{id}/`         | Manage a loan application.                             |
| POST                 | `/api/v1/finance/loans/{id}/submit/`  | Submit a draft loan application for review.            |
| GET/POST             | `/api/v1/finance/kyc-documents/`      | List or upload KYC documents.                          |
| GET/PUT/PATCH/DELETE | `/api/v1/finance/kyc-documents/{id}/` | Manage a KYC document.                                 |
| GET                  | `/api/v1/finance/emi-schedule/`       | List EMI schedule entries (`?application_id=` filter). |
| PATCH                | `/api/v1/finance/emi-schedule/{id}/`  | Update an EMI schedule entry.                          |
| POST                 | `/api/v1/finance/emi-schedule/bulk/`  | Replace an application's EMI schedule in bulk.         |

## Subscriptions & Payments

| Method               | Path                                               | Description                                                           |
| -------------------- | -------------------------------------------------- | --------------------------------------------------------------------- |
| GET/POST             | `/api/v1/subscriptions/plans/`                     | List or create subscription plans (`?is_active=` filter, `?search=`). |
| GET/PUT/PATCH/DELETE | `/api/v1/subscriptions/plans/{id}/`                | Manage a subscription plan.                                           |
| GET/POST             | `/api/v1/subscriptions/subscriptions/`             | List or create subscriptions for the user.                            |
| GET/PUT/PATCH/DELETE | `/api/v1/subscriptions/subscriptions/{id}/`        | Manage a subscription.                                                |
| POST                 | `/api/v1/subscriptions/subscriptions/{id}/cancel/` | Cancel a subscription.                                                |
| GET/POST             | `/api/v1/subscriptions/payments/`                  | List or record payments.                                              |
| GET/PUT/PATCH/DELETE | `/api/v1/subscriptions/payments/{id}/`             | Manage a payment record.                                              |

## Chat

| Method               | Path                         | Description                                                  |
| -------------------- | ---------------------------- | ------------------------------------------------------------ |
| GET/POST             | `/api/v1/chat/threads/`      | List or create chat threads.                                 |
| GET/PUT/PATCH/DELETE | `/api/v1/chat/threads/{id}/` | Manage a chat thread.                                        |
| GET/POST             | `/api/v1/chat/messages/`     | List or send chat messages (`?thread_id=` filter supported). |

## WebSocket

| Protocol     | Path                    | Description                                           |
| ------------ | ----------------------- | ----------------------------------------------------- |
| WS/Secure WS | `/ws/chat/{thread_id}/` | Real-time chat channel (authenticate with JWT token). |
