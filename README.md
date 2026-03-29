# Diet-AI Server

- Diet-AI helps the user to track the nutrient intake by taking inputs from the user and guide the user to maintain a balanced diet.
- Diet-AI leverages **AI Agents** to take smart decisions.
- At the beginning, user will be asked with a timeframe. Once timeframe is set, then Diet-AI will track the user and guide the user towards balanced diet over that timeframe.
- **Score** is provided to each user based on the current performance. Our **Scoring Algorithm** is very strict. So there won't be any chance to cheat.

**YOU CAN'T CHEAT!**

### What can user do?

- User can give food intake information in the form of query. Eg: "Hey Today I ate Idli with coconut chutney."
- User can ask any kind of food related questions, or any kind of generic questions or can have normal chit-chat.
- User can ask for diet-suggestions. **Diet Builder Agent** analyses the current nutrient intake levels and suggests some foods to consume to move a step towards balanced diet.
- User can ask for the review. **Nutri Reflector Agent** analyses the current nutrient intake levels and passes comments about the current performance.

Hosted Server Link: https://dietvite-server.onrender.com/

---

### Flow diagram

![Screenshot of Organisation Dashboard ](./assets/Diet%20Vite%20flow%20diagram.png)

### Special Scoring mechanism

Our scoring system is designed to be **strict, fair, and resistant to manipulation**. It evaluates user behavior across multiple dimensions and uses mathematical models to prevent cheating while rewarding consistency.

---

### 🚫 Anti-Cheating Protection (3 Types)

- **Overconsumption Cheating Prevention**
  - Users cannot compensate by overeating certain nutrients.
  - Any intake beyond the ideal value is penalized heavily.
  - High-risk nutrients (Calories, Sodium, Iron, etc.) are penalized even more strictly.
  - Large deviations are punished disproportionately to prevent extreme behavior.

- **Frequency Manipulation Prevention**
  - Users cannot inflate their score by logging excessive meals.
  - Ideal eating frequency is enforced.
  - If daily logs exceed a safe threshold, the day is flagged as suspicious.
  - Encourages realistic and healthy eating patterns.

- **Missing Data / Selective Logging Prevention**
  - Users cannot skip bad days to improve their score.
  - Missing entries directly reduce the score.
  - Ensures consistency and honesty in tracking.

---

### 🎯 Discipline Bonus

- Users are rewarded for **staying consistent over time**, not just short-term performance.
- The more days a user logs data, the higher the bonus.
- Uses a **logarithmic growth model**, meaning:
  - Early consistency gives noticeable rewards
  - Long-term consistency gives steady but controlled improvement
- Bonus is **capped**, so users cannot exploit long durations unfairly.
- Contributes up to **20% of the final score**, making consistency a key factor.
- Encourages building **sustainable healthy habits instead of temporary spikes**.

---

### 🧠 Mathematical Techniques Used

- **Exponential Decay Function**
  - Formula: `score = exp(-penalty * deviation)`
  - Small deviations → small penalty
  - Large deviations → sharp score drop
  - Ensures accuracy is rewarded while discouraging extremes

- **Quadratic Penalty (Power Function)**
  - Formula: `overshoot_factor²`
  - Heavily penalizes large overconsumption
  - Prevents balancing good and bad days artificially

- **Weighted Averaging System**
  - Nutrient Accuracy → 70%
  - Frequency Discipline → 20%
  - Logging Consistency → 10%
  - Discipline Bonus → additional 20% influence on final score
  - Ensures balanced evaluation across multiple behaviors

- **Logarithmic Growth (Consistency Bonus)**
  - Formula: `log(1 + days)`
  - Smooth and capped growth curve
  - Prevents exploitation while rewarding dedication

- **Normalization**
  - All intermediate scores are scaled between 0 and 1
  - Final score is scaled to 0–100 for readability

---

### 🔐 Why This System is Hard to Cheat

- Non-linear penalties make extreme behavior ineffective
- Skipping logs reduces score directly
- Over-logging is detected and penalized
- Consistency is rewarded, so short bursts don’t help much
- Multiple scoring dimensions prevent single-point exploitation

---

### ✅ Summary

- Overeating manipulation → Prevented
- Skipping bad days → Penalized
- Fake logging behavior → Detected
- Inconsistent tracking → Lower rewards
- Long-term discipline → Rewarded

**Result:** A robust scoring system that rewards genuine healthy habits, consistency, and long-term discipline — not shortcuts.

---

### How to use the APIs?

- Paste the [hosted server link](https://dietvite-server.onrender.com/) in the browser and add "/docs" at the end of the link and click on it.
- It will lead you to the Swagger UI where you can play around with the APIs.

### List of APIs

- `POST /signup` (For Signing up)
- `POST /login` (For Logging in)
- `GET /logout` (For Logging out)
- `POST /start` (Takes Query and passes comments)
- `GET /diet_suggestions` (returns the diet suggestions)
- `GET /review` (returns current performance remarks)
- `GET /check_skips` (gets scolded for skipping)
- `GET /calculate_score` (gets user's score)
- `GET /get_user_stats` (returns the user's statistics)
- `GET /reset` (resets the timeframe and user state)

---

### List of Agents

- `Nutri Orchestrator` - decides whether user query is generic or anything related to user's food consumption.
- `Omni Knowledge Bot` - answers any kind of questions and interacts with the user.
- `Nutri Scanner` - analyses the nutrients consumed based on the food intake query passed by the user and updates the overall nutrient sheet values for that user.
- `Diet Builder` - analyses the gap between current nutrient consumed and balanced diet levels and suggest food to move towards the balanced diet.
- `Nutri Reflector` - reviews the current nutrient intake levels and passes down the comments regarding your performance.
- `Missy Monitor` - scolds the user if the user missed to provide info about the food consumed on any date.

---

- For obvious reasons I haven't provided any prompts in the codes.
- Follow the config.py for the .env structure

---

## 👥 Contributors

- [Vinay Yadam](https://github.com/YadamVinay369)
- [Vethan Yadam](https://github.com/vethan143)

---

## 📄 License

This project is licensed under the MIT License.

Copyright (c) 2026 Vinay Yadam, Vethan Yadam

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies.

See the full license details in the [LICENSE](./LICENSE) file.
