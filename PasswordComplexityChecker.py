{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOx29UypL+05h+YZvWL88oZ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ProjectApi2024/EliteTech-Intern/blob/main/PasswordComplexityChecker.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#Password Complexity Checker Program"
      ],
      "metadata": {
        "id": "zBBJw2SqtCX1"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "import re\n",
        "\n",
        "def password_complexity_checker(password):\n",
        "\n",
        "    # Check length\n",
        "\n",
        "    length_score = len(password) >= 8\n",
        "\n",
        "    # Check for uppercase letters\n",
        "\n",
        "    uppercase_score = bool(re.search(r'[A-Z]', password))\n",
        "\n",
        "    # Check for lowercase letters\n",
        "\n",
        "    lowercase_score = bool(re.search(r'[a-z]', password))\n",
        "\n",
        "    # Check for numbers\n",
        "\n",
        "    number_score = bool(re.search(r'[0-9]', password))\n",
        "\n",
        "    # Check for special characters\n",
        "\n",
        "    special_char_score = bool(re.search(r'[!@#$%^&*(),.?\":{}|<>]', password))\n",
        "\n",
        "    # Calculate total score\n",
        "\n",
        "    total_score = length_score + uppercase_score + lowercase_score + number_score + special_char_score\n",
        "\n",
        "    # Provide feedback based on total score\n",
        "\n",
        "    if total_score == 5:\n",
        "        return \"Strong password\"\n",
        "    elif total_score >= 3:\n",
        "        return \"Good password\"\n",
        "    else:\n",
        "        return \"Weak password\"\n",
        "\n",
        "password = input(\"Enter your password: \")\n",
        "strength = password_complexity_checker(password)\n",
        "print(f\"Password strength: {strength}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "w5rXGp_OtME6",
        "outputId": "901f7c0e-bf6d-4cd2-e5d1-e854965072b5"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter your password: ADC@123\n",
            "Password strength: Good password\n"
          ]
        }
      ]
    }
  ]
}