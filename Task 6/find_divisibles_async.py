import asyncio  # Import the asyncio module
import time


async def async_find_divisibles(in_range, divisor):
    start_time = time.time()
    print(f"async_find_divisibles called with range {in_range} and divisor {divisor}")
    divisible_numbers = []
    for i in range(1, in_range + 1):
        if i % divisor == 0:
            divisible_numbers.append(i)
            await asyncio.sleep(0)      # Move control to the event loop
    end_time = time.time()
    print(f"async_find_divisibles ended with range {in_range} and divisor {divisor}. It took {end_time - start_time} seconds")
    return divisible_numbers

async def main():
    task1 = asyncio.create_task(async_find_divisibles(50800000, 34113))
    task2 = asyncio.create_task(async_find_divisibles(100052, 3210))
    task3 = asyncio.create_task(async_find_divisibles(500, 3))
    

    await task1                 # Wait for the task to complete
    result2 = await task2       # Wait for the task to complete
    result3 = await task3       # Wait for the task to complete
    
    print(result2)
    print(result3)

if __name__ == "__main__":
    asyncio.run(main())
