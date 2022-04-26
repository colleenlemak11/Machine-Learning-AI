from pomegranate import *

electronic = Node(DiscreteDistribution {(
    "electronic failure": 0.1,
    "no electronic failure" : 0.9
)}, name="electronic"

# engine failure is an unconditional distribution: P(engine)

engine = Node(DiscreteDistribution ({
    "engine failure": 0.2
    "no engine failure":0.8
)}, name="engine"
              
car_failure = Node(ConditionalProbabilityTable ({
    ["electronic failure"]
}