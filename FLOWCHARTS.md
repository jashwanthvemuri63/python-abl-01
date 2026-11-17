# Flowcharts

These flowcharts are reference designs for the ten selected integrated case studies. The Mermaid syntax renders on GitHub. Adjust any branch or rule that differs from the final program.

## Case study 91

**Advanced String-Based Registration Record Analyzer**

```mermaid
flowchart TD
    A([Start]) --> B[/Read record strings/]
    B --> C[Split each record into fields]
    C --> D{Correct field count and formats?}
    D -- No --> E[Report malformed record]
    D -- Yes --> F{Identifier already seen?}
    F -- Yes --> G[Report duplicate identifier]
    F -- No --> H[Extract fields and classify record]
    E --> I{More records?}
    G --> I
    H --> I
    I -- Yes --> C
    I -- No --> J[/Print valid records and errors/]
    J --> K([End])
```

## Case study 92

**Multi-Event Sports Scheduling and Scoring**

```mermaid
flowchart TD
    A([Start]) --> B[/Read teams, schedule tuples, and match scores/]
    B --> C[Check each event against earlier events]
    C --> D{Team scheduled twice in same period?}
    D -- Yes --> E[Record schedule conflict]
    D -- No --> F[Accept schedule entry]
    E --> G[Initialize each team's points and goal difference]
    F --> G
    G --> H[Process each match result]
    H --> I[Update points and goal difference]
    I --> J{More matches?}
    J -- Yes --> H
    J -- No --> K[Rank by points, then goal difference]
    K --> L[/Print conflicts and final rankings/]
    L --> M([End])
```

## Case study 93

**Smart Public Transport Fare Reconciliation**

```mermaid
flowchart TD
    A([Start]) --> B[/Read routes and passenger counts by category/]
    B --> C[Set expected revenue to zero]
    C --> D[Select next route and passenger category]
    D --> E[Multiply count by category fare]
    E --> F[Add fare to expected revenue]
    F --> G{More categories or routes?}
    G -- Yes --> D
    G -- No --> H[/Read collected revenue/]
    H --> I[Calculate difference = collected - expected]
    I --> J{Difference is zero?}
    J -- Yes --> K[Report reconciled]
    J -- No --> L[Report discrepancy]
    K --> M([End])
    L --> M
```

## Case study 94

**Disaster Relief Supply Allocation**

```mermaid
flowchart TD
    A([Start]) --> B[/Read stock and area requirements/]
    B --> C[Order areas by supplied priority]
    C --> D[Select next area and supply type]
    D --> E[Allocate minimum of stock and demand]
    E --> F[Subtract allocation from stock and demand]
    F --> G{More supplies or areas?}
    G -- Yes --> D
    G -- No --> H[Calculate unmet demand]
    H --> I[/Print allocations, remaining stock, and unmet demand/]
    I --> J([End])
```

## Case study 95

**Integrated Manufacturing Production Planner**

```mermaid
flowchart TD
    A([Start]) --> B[/Read product demand, material use, stock, defects, and limits/]
    B --> C[Calculate required material for each product]
    C --> D[Add required material to total]
    D --> E{More products?}
    E -- Yes --> C
    E -- No --> F[Compare total requirement with available stock]
    F --> G[Calculate shortage or surplus]
    G --> H[Calculate defect percentage per batch]
    H --> I{Any defect rate above limit?}
    I -- Yes --> J[Flag quality violation]
    I -- No --> K[Mark quality within limit]
    J --> L[/Print feasibility, material balance, and quality report/]
    K --> L
    L --> M([End])
```

## Case study 96

**Multi-Criteria Library Resource Distribution**

```mermaid
flowchart TD
    A([Start]) --> B[/Read book copies, branch demands, and priorities/]
    B --> C[Order branches by priority]
    C --> D[Select next book and branch]
    D --> E[Allocate minimum of copies and demand]
    E --> F[Update copies and unmet demand]
    F --> G{More branches or books?}
    G -- Yes --> D
    G -- No --> H[Summarize fulfilled and unmet demand]
    H --> I[/Print distribution report/]
    I --> J([End])
```

## Case study 97

**Smart Campus Incident and Maintenance Prioritization**

```mermaid
flowchart TD
    A([Start]) --> B[/Read incident severity, location priority, and frequency/]
    B --> C[Calculate score = 3 x severity + 2 x location priority + frequency]
    C --> D[Store incident and score]
    D --> E{More incidents?}
    E -- Yes --> B
    E -- No --> F[Rank incidents by score, highest first]
    F --> G[/Print ranked incident list/]
    G --> H([End])
```

## Case study 98

**University Academic Progression Audit**

```mermaid
flowchart TD
    A([Start]) --> B[/Read student marks, attendance, and prerequisites/]
    B --> C[Create empty list of unmet conditions]
    C --> D[Check each subject mark against pass mark]
    D --> E{Any subject below pass mark?}
    E -- Yes --> F[Add failed subject to reasons]
    E -- No --> G[Check attendance threshold]
    F --> G
    G --> H{Attendance below threshold?}
    H -- Yes --> I[Add attendance to reasons]
    H -- No --> J[Check prerequisites]
    I --> J
    J --> K{Prerequisite incomplete?}
    K -- Yes --> L[Add prerequisite to reasons]
    K -- No --> M[Keep existing reasons]
    L --> N{Reasons list empty?}
    M --> N
    N -- Yes --> O[Mark eligible for progression]
    N -- No --> P[Mark not eligible]
    O --> Q[/Print status and reasons/]
    P --> Q
    Q --> R([End])
```

## Case study 99

**Integrated E-Commerce Order Processing and Reconciliation**

```mermaid
flowchart TD
    A([Start]) --> B[/Read product stock, orders, dispatches, and returns/]
    B --> C[Check each order against product and quantity records]
    C --> D{Order or dispatch data inconsistent?}
    D -- Yes --> E[Record discrepancy]
    D -- No --> F[Calculate pending quantity]
    F --> G[Update stock for dispatched and returned items]
    G --> H[Calculate net delivered quantity and revenue]
    E --> I{More orders?}
    H --> I
    I -- Yes --> C
    I -- No --> J[/Print revenue, pending orders, discrepancies, and stock/]
    J --> K([End])
```

## Case study 100

**Comprehensive Smart Campus Management Simulation**

```mermaid
flowchart TD
    A([Start]) --> B[Initialize student, attendance, marks, event, and resource lists]
    B --> C[/Display menu and read choice/]
    C --> D{Choice}
    D -- Student record --> E[Validate and store student details]
    D -- Attendance --> F[Update attendance record]
    D -- Marks --> G[Store marks and calculate result]
    D -- Event --> H[Validate registration and update entry list]
    D -- Resources --> I[Check demand against available resources]
    D -- Summary --> J[Calculate and display campus summary]
    D -- Exit --> K([End])
    E --> L{Exit selected?}
    F --> L
    G --> L
    H --> L
    I --> L
    J --> L
    L -- No --> C
    L -- Yes --> K
```
