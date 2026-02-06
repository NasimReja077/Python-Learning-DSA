import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


# 🔹 Get All Posts
def get_all_posts():
    response = requests.get(BASE_URL)
    if response.status_code == 200:
        posts = response.json()
        print("\n--- All Posts (First 5) ---")
        for post in posts[:5]:
            print(f"ID: {post['id']} | Title: {post['title']}")
    else:
        print("Error fetching posts")


# 🔹 Get Single Post
def get_single_post():
    post_id = input("Enter Post ID: ")
    response = requests.get(f"{BASE_URL}/{post_id}")
    
    if response.status_code == 200:
        post = response.json()
        print("\n--- Post Details ---")
        print("Title:", post["title"])
        print("Body:", post["body"])
    else:
        print("Post not found!")


# 🔹 Create New Post
def create_post():
    title = input("Enter Title: ")
    body = input("Enter Body: ")

    payload = {
        "title": title,
        "body": body,
        "userId": 1
    }

    response = requests.post(BASE_URL, json=payload)

    if response.status_code == 201:
        print("\nPost created successfully!")
        print("Response:", response.json())
    else:
        print("Error creating post")


# 🔹 Delete Post
def delete_post():
    post_id = input("Enter Post ID to delete: ")
    response = requests.delete(f"{BASE_URL}/{post_id}")

    if response.status_code == 200:
        print("Post deleted successfully!")
    else:
        print("Error deleting post")


# 🔹 Main Menu
def main():
    while True:
        print("\n===== Post Manager =====")
        print("1. Get All Posts")
        print("2. Get Single Post")
        print("3. Create Post")
        print("4. Delete Post")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            get_all_posts()
        elif choice == "2":
            get_single_post()
        elif choice == "3":
            create_post()
        elif choice == "4":
            delete_post()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
