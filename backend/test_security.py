from app.security.risk_engine import RiskEngine


def main():
    engine = RiskEngine()
    result = engine.evaluate(
        tool="database",
        action="delete all users"
    )
    print(result)


if __name__ == "__main__":
    main()
