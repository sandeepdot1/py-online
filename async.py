import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulates a time-consuming I/O task
    print("Data fetched")
    return "some data"

async def task1():
    await asyncio.sleep(3)
    print("Task 1 done")
    return "result 1"

async def task2():
    await asyncio.sleep(1)
    print("Task 2 done")
    return "result 2"

async def main():
    print("Starting main function")
    # Create a task for fetch_data and run it in the background
    task = asyncio.create_task(fetch_data())
    print("Do other stuff while waiting for data")
    
    # Optionally, you can await the task to get its result
    result = await task  # Wait for task completion
    print(f"Result: {result}")

    # Run both tasks concurrently (using gather())
    results = await asyncio.gather(task1(), task2())
    print(f"Results: {results}")

# asyncio.run(main())

async def failing_task():
    await asyncio.sleep(1)
    raise ValueError("Something went wrong!")

async def successful_task():
    await asyncio.sleep(2)
    return "Success!"

async def main1():
    task1 = asyncio.create_task(failing_task())
    task2 = asyncio.create_task(successful_task())
    
    # Handle both tasks concurrently
    await asyncio.sleep(1.5)  # Let the tasks run for a while

    # Check if the first task raised an exception
    if task1.done():
        try:
            print("printing task1 result")
            result = task1.result()  # Will raise the exception if it failed
        except ValueError as e:
            print(f"Task 1 failed with: {e}")
    
    # Await the second task to get its result
    result2 = await task2
    print(f"Task 2 completed with result: {result2}")

# asyncio.run(main1())


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({number}), currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")
    return f

async def main2():
    # Schedule three calls *concurrently*:
    L = await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
    )
    print(L)

asyncio.run(main2())


