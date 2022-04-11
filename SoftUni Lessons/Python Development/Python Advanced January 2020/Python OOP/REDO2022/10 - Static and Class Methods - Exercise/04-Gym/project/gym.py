from project.customer import Customer
from project.trainer import Trainer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        # add the customer in the customer list, if the customer is not already in it.
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        # add the trainer to the trainers list, if the trainer is not already in it
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        # add the equipment to the equipment list, if the equipment is not already in it
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        # add the plan to the plans list, if the plan is not already in it
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        # add the subscription in the subscriptions list, if the subscription is not already in it
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        sub_found = [s for s in self.subscriptions if s.id == subscription_id]
        if sub_found:
            result = ''
            subscription = sub_found[0]
            customer = [c for c in self.customers if c.id == subscription.customer_id][0]
            trainer = [t for t in self.trainers if t.id == subscription.trainer_id][0]
            plan = [p for p in self.plans if p.id == subscription.exercise_id][0]
            equipment = [e for e in self.equipment if e.id == plan.equipment_id][0]
            result += f"{str(subscription)}\n"
            result += f"{str(customer)}\n"
            result += f"{str(trainer)}\n"
            result += f"{str(equipment)}\n"
            result += f"{str(plan)}"
            return result

total_price = 7.2
total_price = f"{total_price:.2f}"

# customer = Customer("John", "Maple Street", "john.smith@gmail.com")
# equipment = Equipment("Treadmill")
# trainer = Trainer("Peter")
# subscription = Subscription("14.05.2020", 1, 1, 1)
# plan = ExercisePlan(1, 1, 20)
#
# gym = Gym()
#
# gym.add_customer(customer)
# gym.add_equipment(equipment)
# gym.add_trainer(trainer)
# gym.add_plan(plan)
# gym.add_subscription(subscription)
#
# print(Customer.get_next_id())
#
# print(gym.subscription_info(1))
