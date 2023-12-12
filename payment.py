import stripe

# Set your Stripe API key
stripe.api_key = 'stripe key'

def make_payment():
    global name;name=input("Enter your name: ")
    global email;email=input("Enter email: ")
    card_number = input("Enter card number: ")
    exp_month = input("Enter expiration month: ")
    exp_year = input("Enter expiration year: ")
    cvc = input("Enter CVC: ")
    currncy=input("Enter currency ie. dollars or inr (please ensure you enter the correct spelling): ")
    currncy=currncy.lower()
    # Create a payment token
    token = stripe.Token.create(
        card={
            "number": card_number,
            "exp_month": exp_month,
            "exp_year": exp_year,
            "cvc": cvc,
        },
    )

    try:
        if currncy=='dollars':
            amt=input("Enter amount to be payed in dollars: ")
            amt_cnvrt=amt*100
            charge = stripe.Charge.create(
                amount=amt_cnvrt,
                currency='usd',
                description='put descriotion here',
                source=token.id,
            )
            print("Payment successful!")
        if currncy=='inr':
            amt=input("Enter amount to be payed in INR: ")
            charge=stripe.Charge.create(
                amount=amt,
                currency='inr',
                description= 'put description here',
                source=token.id,
            )
        else:
            print("Please choose a either inr or dollars(if you have chosen out of these 2 and still see this message then please recheck the spelling)")
    
    except stripe.error.CardError as e:
        # The card has been declined
        print(f"Payment failed: {e}")

if __name__ == '__main__':
    make_payment()
