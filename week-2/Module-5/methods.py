
class Phone:
    model = "A15"
    price = 20000
    features = ['camera', 'sensors', 'smoth-performance','best bettary']
    def call(self, phone_number, sms):
        text = f"Callind on number {phone_number} with message {sms}"
        return text

my_phone = Phone()
print(my_phone.features)
print(my_phone.call('1729107200', 'Yeah, Do your best what ever do doing'))


# Class
# -------
# In class variable are attributes
# In class function are methods
 
