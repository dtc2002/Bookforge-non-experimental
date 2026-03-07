{
  "type": "object",
  "required": [
    "title",
    "genre",
    "target_audience",
    "tone",
    "length_target"
  ],
  "properties": {
    "title": {
      "type": "string",
      "minLength": 1
    },

    "genre": {
      "type": "string",
      "minLength": 1
    },

    "subgenre": {
      "type": "string"
    },

    "target_audience": {
      "type": "string",
      "enum": [
        "middle_grade",
        "young_adult",
        "new_adult",
        "adult"
      ]
    },

    "tone": {
      "type": "string",
      "minLength": 1
    },

    "length_target": {
      "type": "string",
      "enum": [
        "short_story",
        "novella",
        "novel"
      ]
    },

    "complexity_preference": {
      "type": "string",
      "enum": [
        "minimal",
        "tight",
        "moderate",
        "rich"
      ]
    },

    "intended_emotional_effect": {
      "type": "string"
    },

    "market_intent": {
      "type": "string",
      "enum": [
        "personal",
        "reader_facing",
        "commercial",
        "serial_web_fiction"
      ]
    },

    "series_intent": {
      "type": "string",
      "enum": [
        "standalone",
        "possible_series",
        "planned_series",
        "serial"
      ]
    },

    "pov_preference": {
      "type": "string",
      "enum": [
        "first_person",
        "third_person_limited",
        "third_person_omniscient",
        "multiple_pov",
        "no_preference"
      ]
    },

    "tense_preference": {
      "type": "string",
      "enum": [
        "past",
        "present",
        "no_preference"
      ]
    },

    "ending_preference": {
      "type": "string",
      "enum": [
        "closed_win",
        "closed_loss",
        "bittersweet",
        "open_but_stable",
        "sequel_hook",
        "no_preference"
      ]
    },

    "pacing_preference": {
      "type": "string",
      "enum": [
        "fast",
        "moderate",
        "immersive",
        "no_preference"
      ]
    },

    "content_boundaries": {
      "type": "object",
      "properties": {
        "violence": {
          "type": "string",
          "enum": [
            "none",
            "very_low",
            "low",
            "moderate",
            "high"
          ]
        },
        "romance": {
          "type": "string",
          "enum": [
            "none",
            "light",
            "moderate",
            "high"
          ]
        },
        "sexual_content": {
          "type": "string",
          "enum": [
            "none",
            "fade_to_black",
            "moderate",
            "explicit"
          ]
        },
        "language": {
          "type": "string",
          "enum": [
            "none",
            "mild",
            "moderate",
            "strong"
          ]
        },
        "horror_intensity": {
          "type": "string",
          "enum": [
            "none",
            "light",
            "moderate",
            "high"
          ]
        }
      },
      "additionalProperties": false
    },

    "required_elements": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },

    "forbidden_elements": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },

    "taboo_elements": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },

    "comparative_feel": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },

    "originality_constraints": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },

    "story_hook": {
      "type": "string"
    },

    "premise_seed": {
      "type": "string"
    },

    "setting_seed": {
      "type": "string"
    },

    "character_seed": {
      "type": "string"
    },

    "conflict_seed": {
      "type": "string"
    },

    "operator_notes": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },

    "universe_bible": {
      "type": "string"
    },

    "universe_mode": {
      "type": "string",
      "enum": [
        "original",
        "existing_bible"
      ]
    }
  },

  "additionalProperties": false
}