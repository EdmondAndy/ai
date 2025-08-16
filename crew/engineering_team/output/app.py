import gradio as gr
from accounts import Account

# Initialize the account for the demo
acc = Account(account_id=1, initial_deposit=10000)

def create_account(initial_deposit):
    global acc
    acc = Account(account_id=1, initial_deposit=float(initial_deposit))
    return f"Account created with initial deposit: ${initial_deposit}"

def deposit_funds(amount):
    amount = float(amount)
    success = acc.deposit(amount)
    return f"Deposit {'successful' if success else 'failed'}: ${amount}. Current Balance: ${acc.balance}"

def withdraw_funds(amount):
    amount = float(amount)
    success = acc.withdraw(amount)
    return f"Withdrawal {'successful' if success else 'failed'}: ${amount}. Current Balance: ${acc.balance}"

def buy_shares(symbol, quantity):
    quantity = int(quantity)
    success = acc.buy_shares(symbol, quantity)
    return f"Buy {'successful' if success else 'failed'}: {quantity} shares of {symbol}. Current Balance: ${acc.balance}"

def sell_shares(symbol, quantity):
    quantity = int(quantity)
    success = acc.sell_shares(symbol, quantity)
    return f"Sell {'successful' if success else 'failed'}: {quantity} shares of {symbol}. Current Balance: ${acc.balance}"

def view_portfolio_value():
    value = acc.calculate_portfolio_value()
    return f"Total Portfolio Value: ${value}"

def view_profit_or_loss():
    profit_or_loss = acc.calculate_profit_or_loss()
    return f"Profit or Loss: ${profit_or_loss}"

def view_holdings():
    holdings = acc.get_holdings()
    return f"Current Holdings: {holdings}"

def view_transactions():
    transactions = acc.get_transaction_history()
    return f"Transaction History: {transactions}"

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# Simple Trading Platform Interface")
    with gr.Tab("Account Management"):
        with gr.Row():
            initial_deposit = gr.Number(label="Initial Deposit")
            create_btn = gr.Button("Create Account")
            create_btn.click(create_account, initial_deposit, gr.Textbox(label="Account Status"))

        with gr.Row():
            deposit_amount = gr.Number(label="Deposit Amount")
            deposit_btn = gr.Button("Deposit Funds")
            deposit_btn.click(deposit_funds, deposit_amount, gr.Textbox(label="Deposit Status"))
        
        with gr.Row():
            withdraw_amount = gr.Number(label="Withdraw Amount")
            withdraw_btn = gr.Button("Withdraw Funds")
            withdraw_btn.click(withdraw_funds, withdraw_amount, gr.Textbox(label="Withdrawal Status"))
    
    with gr.Tab("Trading"):
        with gr.Row():
            symbol = gr.Textbox(label="Stock Symbol")
            quantity = gr.Number(label="Quantity")
            buy_btn = gr.Button("Buy Shares")
            buy_btn.click(buy_shares, [symbol, quantity], gr.Textbox(label="Buy Status"))
        
        with gr.Row():
            symbol = gr.Textbox(label="Stock Symbol")
            quantity = gr.Number(label="Quantity")
            sell_btn = gr.Button("Sell Shares")
            sell_btn.click(sell_shares, [symbol, quantity], gr.Textbox(label="Sell Status"))
    
    with gr.Tab("Portfolio"):
        with gr.Row():
            portfolio_value_btn = gr.Button("View Portfolio Value")
            portfolio_value_btn.click(view_portfolio_value, outputs=gr.Textbox(label="Portfolio Value"))
        
        with gr.Row():
            profit_loss_btn = gr.Button("View Profit/Loss")
            profit_loss_btn.click(view_profit_or_loss, outputs=gr.Textbox(label="Profit/Loss"))
        
        with gr.Row():
            holdings_btn = gr.Button("View Holdings")
            holdings_btn.click(view_holdings, outputs=gr.Textbox(label="Holdings"))
        
        with gr.Row():
            transactions_btn = gr.Button("View Transactions")
            transactions_btn.click(view_transactions, outputs=gr.Textbox(label="Transaction History"))

if __name__ == "__main__":
    demo.launch()