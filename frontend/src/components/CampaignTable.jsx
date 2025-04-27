export default function CampaignTable({ data }) {
    return (
      <div className="overflow-x-auto">
        <table className="min-w-full bg-white shadow rounded-lg">
          <thead className="bg-gray-100">
            <tr>
              {["Name","Status","Clicks","Cost","Impressions"].map(h => (
                <th key={h} className="px-4 py-2 text-left text-sm font-medium text-gray-600">
                  {h}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {data.map(c => (
              <tr key={c.id} className="hover:bg-gray-50">
                <td className="px-4 py-2">{c.name}</td>
                <td className="px-4 py-2">{c.status}</td>
                <td className="px-4 py-2">{c.clicks}</td>
                <td className="px-4 py-2">${c.cost.toFixed(2)}</td>
                <td className="px-4 py-2">{c.impressions}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }
  